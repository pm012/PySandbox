"""
Your program should meet the following requirements:

Write a function or method called find that takes two arguments called 
path and dir. The path argument should accept a relative or absolute path to a 
directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path.
Your program should display the absolute paths if it finds a directory with the given name.
The directory search should be done recursively. This means that the search should also include all subdirectories in the given path.
Example input:

path="./tree", dir="python"

Example output:

Output
.../tree/python
.../tree/cpp/other_courses/python
.../tree/c/other_courses/python
"""


import os

class DirectorySearcher:
    def __init__(self):
        self.start_path = None
        self.base = None

    def find(self, path, dir):
        path = os.path.abspath(path)
        if self.start_path is None:
            self.start_path = path
        if self.base is None:
            self.base = os.path.basename(os.path.normpath(path)) # <--extract "tree"

        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                if entry == dir:                    
                    # get path relative to the original starting point
                    rel = os.path.relpath(entry_path, start=os.path.abspath(self.start_path))
                    print(f"...{self.base}/{rel}")
                # Recurse into subdirectories
                self.find(entry_path, dir)



if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(script_dir, "lab_4_4_8")
    os.chdir(dir_path)
    
    # Create an instance of DirectorySearcher and search for directories named "python"
directory_searcher = DirectorySearcher()
directory_searcher.find("./tree", "python")
    