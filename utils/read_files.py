import os
import glob

def read_file(file):
    print(file)
            
    if os.path.isfile(file):
        text_file = open(file, "r")

        text = text_file.read()

        text_file.close()

        return text
    
    return ""

def read_paths(paths):
    print("Reading files...")

    str_files = ""
    for path in paths:
        for file in glob.iglob(path + '/**', recursive=True):
            str_files = str_files + os.linesep + read_file(file)
    
    return str_files