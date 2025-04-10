from sys import path
from pathlib import Path
# path.append('../packages') - different for Windows and POSIX
packages_path = Path(__file__).resolve().parent.parent / "packages" # solution will work both for POSSIX and Windows
path.append(str(packages_path))

#from extra.iota import FunI
import extra.iota 
import extra.good.best.sigma
from extra.good.best.tau import FunT

#print(FunI())
print(extra.iota.FunI())
print(extra.good.best.sigma.FunS())
print(FunT())