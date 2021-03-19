


class Logger():
    def __init__(self, file_path):
        self.fp = open(file_path, 'a+')

    def write(self, str_info):
        self.fp.write(str_info)
        self.fp.flush()
    
    def close(self, file_pth):
        self.fp.close()