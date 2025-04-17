from sys import path
from pathlib import Path

# Build path to the zip file (whether on Windows or POSIX)
zip_path = Path(__file__).resolve().parent.parent / "packages" / "extrapack.zip"
path.append(str(zip_path))

from extra.iota import FunI

print(FunI())
