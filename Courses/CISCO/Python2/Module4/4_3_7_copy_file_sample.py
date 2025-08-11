from os import strerror, path
if __name__ == "__main__":
    srcname = input("Enter the source file name: ")
    script_dir = path.dirname(path.abspath(__file__))
    dir_path = path.join(script_dir, 'res')
    src_file_path = path.join(dir_path, srcname)
    try:
        src = open(src_file_path, 'rb')
    except IOError as e:
        print("Cannot open the source file: ", strerror(e.errno))
        exit(e.errno)	

    dstname = input("Enter the destination file name: ")
    dst_file_path = path.join(dir_path, dstname)
    try:
        dst = open(dst_file_path, 'wb')
    except Exception as e:
        print("Cannot create the destination file: ", strerror(e.errno))
        src.close()
        exit(e.errno)	

    buffer = bytearray(65536)
    total  = 0
    try:
        readin = src.readinto(buffer)
        while readin > 0:
            written = dst.write(buffer[:readin])
            total += written
            readin = src.readinto(buffer)
    except IOError as e:
        print("Cannot create the destination file: ", strerror(e.errno))
        exit(e.errno)	
        
    print(total,'byte(s) succesfully written')
    src.close()
    dst.close()