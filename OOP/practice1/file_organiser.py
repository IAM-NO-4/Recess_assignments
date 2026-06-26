
import shutil
import json
import argparse
from pathlib import Path
from datetime import datetime

CATEGORIES = {
    "Images":       [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg",
                     ".webp", ".tiff", ".ico", ".heic", ".raw"],
    "Videos":       [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv",
                     ".webm", ".m4v", ".mpeg", ".3gp"],
    "Audio":        [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a",
                     ".wma", ".opus", ".aiff"],
    "Documents":    [".pdf", ".doc", ".docx", ".odt", ".rtf", ".txt",
                     ".md", ".tex", ".pages"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods", ".numbers"],
    "Presentations":[".ppt", ".pptx", ".odp", ".key"],
    "Archives":     [".zip", ".tar", ".gz", ".bz2", ".xz", ".7z",
                     ".rar", ".iso", ".dmg"],
    "Code":         [".py", ".js", ".ts", ".html", ".css", ".java",
                     ".c", ".cpp", ".h", ".rs", ".go", ".rb", ".php",
                     ".sh", ".bat", ".json", ".xml", ".yaml", ".yml",
                     ".toml", ".sql"],
    "Executables":  [".exe", ".msi", ".apk", ".deb", ".rpm", ".pkg",
                     ".appimage"],
    "Fonts":        [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "Torrents":     [".torrent"],
}

UNDO_LOG = Path.home() / ".downloads_organiser_undo.json"


def ext_to_category() -> dict:
    mapping = {}
    for cat, exts in CATEGORIES.items():
        for ext in exts:
            mapping[ext.lower()] = cat
    return mapping
"taatawo"

def resolve_conflict(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    counter = 1
    while True:
        new_dest = dest.with_name(f"{stem} ({counter}){suffix}")
        if not new_dest.exists():
            return new_dest
        counter += 1


def organise(downloads: Path, dry_run: bool = False, verbose: bool = False):
    if not downloads.is_dir():
        print(f"[ERROR] '{downloads}' is not a valid directory.")
        return

    ext_map   = ext_to_category()
    moves     = []  
    skipped   = []
    errors    = []

    files = [f for f in downloads.iterdir() if f.is_file()]
    print(f"\nScanning: {downloads}")
    print(f"    Found {len(files)} file(s)\n")

    for src in sorted(files):
        ext      = src.suffix.lower()
        category = ext_map.get(ext, "Others")
        dest_dir = downloads / category
        dest     = resolve_conflict(dest_dir / src.name)

        if dry_run:
            print(f"  [DRY-RUN]  {src.name}  →  {category}/")
            moves.append((str(src), str(dest)))
            continue

        try:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(src), str(dest))
            moves.append((str(src), str(dest)))
            if verbose:
                print(f"  {src.name}  →  {category}/")
        except Exception as exc:
            errors.append(src.name)
            print(f" Error: {src.name}  —  {exc}")

    print("\n" + "─" * 50)
    if dry_run:
        print(f"  DRY-RUN complete. {len(moves)} file(s) would be moved.")
        print("  Run without --dry-run to apply changes.")
    else:
        print(f" Moved   : {len(moves)} file(s)")
        if errors:
            print(f" Errors  : {len(errors)} file(s) — {', '.join(errors)}")

        # Save undo log
        log_entry = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "moves": moves,
        }
        existing = []
        if UNDO_LOG.exists():
            try:
                existing = json.loads(UNDO_LOG.read_text())
            except json.JSONDecodeError:
                pass
        existing.append(log_entry)
        UNDO_LOG.write_text(json.dumps(existing, indent=2))
        print(f"\n  Undo log saved → {UNDO_LOG}")
    print("─" * 50 + "\n")


def undo_last(dry_run: bool = False):
    """Reverse the most recent organisation run."""
    if not UNDO_LOG.exists():
        print("[INFO] No undo log found.")
        return

    history = json.loads(UNDO_LOG.read_text())
    if not history:
        print("[INFO] Undo log is empty.")
        return

    last = history[-1]
    print(f"\n Undoing run from {last['timestamp']}")
    print(f"   {len(last['moves'])} move(s) to reverse\n")

    restored = 0
    for src_orig, dest_moved in reversed(last["moves"]):
        dest_path = Path(dest_moved)
        src_path  = Path(src_orig)

        if not dest_path.exists():
            print(f"  [SKIP] Not found: {dest_path.name}")
            continue

        if dry_run:
            print(f"  [DRY-RUN]  {dest_path}  →  {src_path}")
            continue

        try:
            src_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(dest_path), str(src_path))
            restored += 1
        except Exception as exc:
            print(f" Error: {dest_path.name}  —  {exc}")

    if not dry_run:
        # Remove last entry from log
        history.pop()
        UNDO_LOG.write_text(json.dumps(history, indent=2))
        print(f"\nRestored {restored} file(s).")


def main():
    parser = argparse.ArgumentParser(
        description="Organise your Downloads folder into categorised subfolders."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=str(Path.home() / "Downloads"),
        help="Path to the folder to organise (default: ~/Downloads)",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without moving any files",
    )
    parser.add_argument(
        "--undo", "-u",
        action="store_true",
        help="Undo the last organisation run",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Print every file move",
    )
    args = parser.parse_args()

    if args.undo:
        undo_last(dry_run=args.dry_run)
    else:
        organise(Path(args.path), dry_run=args.dry_run, verbose=args.verbose)


if __name__ == "__main__":
    main()