import sys
import shutil

if len(sys.argv) != 2:
    print("Usage: python file_backup.py <filename>")
    sys.exit(1)

src = sys.argv[1]
dst = src + ".backup"
shutil.copy(src, dst)
print(f"Backup created: {dst}")