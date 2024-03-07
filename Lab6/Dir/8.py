import os

path = r"D:\PY\Lab6\Dir\B.txt"

if os.path.exists(path) and os.access(path, os.R_OK) and os.access(path, os.W_OK) and os.access(path, os.X_OK):
    os.remove(path)

else:
    print(f"{path} does not exist")