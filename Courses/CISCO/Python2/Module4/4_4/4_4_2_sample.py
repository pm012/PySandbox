import os

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(script_dir, "res")
    dir_name = os.path.join(dir_path, "new_directory")
    #print(os.uname())
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        print("Directory already exists")
    print(os.listdir(dir_path))
    os.rmdir(dir_name)
    print(os.listdir(dir_path))
    try:
        os.makedirs(f'{dir_path}/my_first_directory/my_second_directory')
    except FileExistsError:
        print("Directory already exists")
    os.chdir(f'{dir_path}/my_first_directory/my_second_directory')
    print(os.listdir(f'{dir_path}/my_first_directory'))
    print(os.getcwd())
    