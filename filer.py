import os, pathlib, socket


def get_machine_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    # print(s.getsockname()[0])
    h_name = s.getsockname()[0]
    s.close()
    return h_name

def all_files(directory):
    for path, dirs, files in os.walk(directory):
        for f in files:
            yield os.path.join(path, f)

video_files = [f for f in all_files('/Users/strongestavenger/Desktop/music')
               if f.endswith(('.mp4', '.flv', '.avi', '.mov', '.wmv'))]

for file in video_files:
    # Convert file-names to urls
    file_url = pathlib.Path(file).as_uri()
    
    namer = get_machine_ip()
    print('http://' + namer + '/' + file_url)
    # print(namer)