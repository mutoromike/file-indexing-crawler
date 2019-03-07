import os, pathlib

def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(path, f)

video_files = [f for f in all_files('/Users/strongestavenger/Desktop/music')
               if f.endswith(('.mp4', '.flv', '.avi', '.mov', '.wmv'))]

for file in video_files:
    # Convert file-names to urls
    file_url = pathlib.Path(file).as_uri()
    print(url_file)