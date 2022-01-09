import os
from src.download import download_files

def check(url, name_file, path_full, lines, error):
    bool_file = os.path.exists(path_full)
    name_not_extension, extension_file = os.path.splitext(name_file)
    folder_path = os.path.split(path_full)[0]

    if bool_file:
        new_name = name_not_extension + str(lines) + extension_file
        new_path = os.path.join(folder_path, new_name)
        download_files(url, new_path, error)
    else:
        download_files(url, path_full, error)