from pathlib import Path

p = Path(Path.home()/"practice_folder")

print(p)
for item in p.iterdir():
    print("Is file: ",item.is_file())
    print("Is folder: ",item.is_dir())
    print(f"{"file name: "if item.is_file() else "folder name: "} {item.name}")
    if item.is_file():
        print("Ext: ", item.suffix)
        print("name: ", item.stem)
    print()

