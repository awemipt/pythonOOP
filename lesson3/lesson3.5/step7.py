class FileAcceptor:
    def __init__(self, *args):
        self.allowedFiles = args

    def __call__(self, filename, *args, **kwargs):
        return filename.split('.')[-1] in self.allowedFiles

    def __add__(self, other):
        return FileAcceptor(*(set(self.allowedFiles + other.allowedFiles)))

acceptor1 = FileAcceptor("jpg", "jpeg", "png")
acceptor2 = FileAcceptor("png", "bmp")
acceptor12 = acceptor1 + acceptor2    # ("jpg", "jpeg", "png", "bmp")
filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]
print(list(filter(acceptor12, filenames)))