import os

def check_dir(name_dir):
    if not os.path.exists(name_dir):
        os.makedirs(name_dir)
        return name_dir
    return name_dir