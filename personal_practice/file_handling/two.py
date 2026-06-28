from pathlib import Path
import shutil

p = Path(Path.home()/"file_practice")
try:    
    p.mkdir(exist_ok=True)
    print(p)
except Exception as e:
    print("Error: ", e)

p2 = Path(p/"Documents")
try:
    p2.mkdir(exist_ok=True)
    print(p2)
except Exception as e:
    print("Error: ", e)

if p.exists():
    file = Path(p/"test.txt")
    try:
        file.touch(exist_ok=True)
        print(file)
    except Exception as e:
        print("Error: ", e)

if file.exists():
    try:
        file.rename(p2/file.name)
        print(f"Moved {file.name} from {file} to {p2}")
    except Exception as e:
        print("Error: ", e)
new_file = Path(p2/"test.txt")
print(f"Old location: {file}")
print(f"New location: {p2}")
print(f"File exists in old location: {file.exists()}")
print(f"File exists in new location: {new_file.exists()}")