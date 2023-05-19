import os, sys
currentFolder = os.path.abspath('')
try:
    sys.path.remove(str(currentFolder))
except ValueError: # Already removed
    pass

# projectFolder = '/home/ababil/BUET/AV/May 2023/AV/src'
# projectFolder = 'C:\\Users\\Zenbook325E\\TTI-dataset-tools\\src'
projectFolder = 'F:/behavior-hypothesis/src'
sys.path.append(str(projectFolder))
os.chdir(projectFolder)
print( f"current working dir{os.getcwd()}")
