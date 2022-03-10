import os


def historically_justified(data_folder):
    data = ''
    files = os.listdir(data_folder)
    for f_ in files:
        with open(f"{data_folder}/{f_}", 'r') as f:
            data += f.read()
    return data
