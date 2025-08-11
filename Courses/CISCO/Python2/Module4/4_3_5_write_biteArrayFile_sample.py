from os import strerror, path, makedirs

if __name__ == "__main__":
    script_path = path.dirname(path.abspath(__file__))
    dir_path = path.join(script_path, 'res')
    file_path = path.join(script_path, 'res/file_4_3_5.bin')
    
    makedirs(dir_path, exist_ok=True)
    
    
    data = bytearray(34)

    for i in range(len(data)):
        data[i] = 10 + i

    try:
        bf = open(file_path, 'wb')
        bf.write(data)
        bf.close()
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))
        
        
    try:
        binary_file = open(file_path, 'rb')
        binary_file.readinto(data)
        binary_file.close()

        for b in data:
            print(bin(b), end=' : ')
            print(int(b), end=' : ')
            print(hex(b), end=' : ')
            print()
    except IOError as e:
        print("I/O error occurred:", strerror(e.errno))