import os

def dir_list(dir_path):
    path_info = list(os.walk(dir_path))[0]
    files = [f for f in path_info[2] if ((not f.startswith('.')) and (not f.endswith('.ini')))]
    dirs = [d for d in path_info[1] if not d.startswith('.')]
    root_dir = path_info[0]

    return [root_dir, dirs, files]

print(dir_list("C:\\Users\\Mauricio\\Desktop\\Prueba\\A"))