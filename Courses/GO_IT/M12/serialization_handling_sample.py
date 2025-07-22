import pickle
import os


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        #attributes = {**self.__dict__}  # The same as above - creates a shallow copy of the attributes dictionary
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])
        
if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "text.txt")
    r = Reader(file_path)
    print(r.read(10))  # reads first 10 characters

    # Save the state to a file
    with open(os.path.join(script_dir, "reader.pkl"), "wb") as f:
        pickle.dump(r, f)
    r.close()

    # Later, resume reading
    with open(os.path.join(script_dir, "reader.pkl"), "rb") as f:
        r2 = pickle.load(f)

    print(r2.read(10))  # continues from where it left off
    r2.close()

