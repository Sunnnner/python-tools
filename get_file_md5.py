import hashlib

def get_file_md5(file):
    md5_value = hashlib.md5()
    while True:
        data_flow = file.file.read(1024)
        if not data_flow:
            break
        md5_value.update(data_flow)
    file_md5 = md5_value.hexdigest()
    return file_md5

if __name__ == "__main__":
    file_md5 = get_file_md5(file)