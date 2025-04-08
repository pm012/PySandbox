# NB! close file after each call to start with the beginning of a file

file_name1 = "res/1.txt"
file_name2 = "res/2.txt"

"""To read file in python open file with the following second parameter:
1. a append - adds the text to the end of file contents
2. w write - rewrites existing text in file
3. r read - read only mode
4. a+ - Open the file for reading and writing. Create a file if it doesn't exist. Otherwise the pointer is at the end of the file
5. w+ - creates a file if the file doesn't exist. Otherwise the file is overwritten
6. r+ - read/write. The pointer is at the beginning of the file
"""

file = open(file_name1, 'r')

"""
file.read(N) - reads the file till the end, N - # of bytes
readline() -  read one entire line from the file
readlines() - returns all the lines in a format of a list. 
If a  parameter provided the lines exceeding the numbers of bytes will not be returned
"""
text = file.readline(10)
text2 = file.readline()
print(text +"!!!!!!!!!!")
print(text2 + "*************8")

"""
write() writes string to an open file
"""
#file.write(" Python is amazing ")
text3 = file.read()
print(text3)

file.close() # close the file


