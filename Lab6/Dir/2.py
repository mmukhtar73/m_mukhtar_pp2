import os

path = r"D:\pp2_assignments\lab6"

if os.path.exists(path):
    print(f"{path} exists")
else:
    print(f"{path} does not exist")

# Test readability
if os.access(path, os.R_OK):
    print(f"{path} is readable")
else:
    print(f"{path} is not readable")

# Test writability
if os.access(path, os.W_OK):
    print(f"{path} is writable")
else:
    print(f"{path} is not writable")

# Test executability
if os.access(path, os.X_OK):
    print(f"{path} is executable")
else:
    print(f"{path} is not executable")