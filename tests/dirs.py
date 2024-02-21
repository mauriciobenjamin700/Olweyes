import os.path as path
import sys

#caminho atual relativo
print(path.curdir)

#caminho atual definitivo
current_dir = path.abspath(path.curdir)
print(current_dir)

# pai do caminho atual
print("dirname x1 = ",path.dirname(current_dir))
#avo do caminho atual
print("dirname x2 = ",path.dirname( path.dirname(current_dir)))





