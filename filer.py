import os

def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            # print(f)
            yield os.path.join(path, f)
            # print(f)

r3d_files = [f for f in all_files('/Users/strongestavenger/Desktop/music')
               if f.endswith('.mp4')]

# print(r3d_files)
for file in r3d_files:
    print(file)