import os

path = r"D:\PY\Lab6"

if os.path.exists(path):
    print(os.path.basename(path)) #filename
    print(os.path.dirname(path)) #directory portion of path in which file exists
else:
    print(f"{path} does not exist")