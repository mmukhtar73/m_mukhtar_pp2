import os

path = r"D:\pp2_assignments\lab6\dir"

print("Only directories:")
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        print(name)

print("Only files:")
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        print(name)

print("All directories and files:")     
for name in os.listdir(path):
    print(name)