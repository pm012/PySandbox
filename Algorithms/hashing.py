import hashlib

def my_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    #secret01
    #print(my_hash('secret01'))
    hash_password = '3064ce319bdba6c59a5610f4bd767cdd557ffed0c700c170c6612fe0863485da'

    input_password = input('Password: ')
    hash_input_password = my_hash(input_password)

    if hash_password == hash_input_password:
        print('You are authorized!')
    else:
        print('Incorrect username or password')
    
