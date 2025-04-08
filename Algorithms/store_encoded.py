from PIL import Image

FILE_NAME = 'out.png'
def code_pix(text):    
    img = Image.new('RGB', (len(text), 1))
    for i in range(len(text)):
        img.putpixel((i, 0), (ord(text[i]), 0, 0))

    img.save(FILE_NAME)

def decodde_pix(fname):
    text = ''
    img = Image.open(fname)
    width, height = img.size

    for i in range(width):
        px = img.getpixel((i,0))
        text += chr(px[0])
    return text


if __name__ == "__main__":
    code_pix('hello world')

    text = decodde_pix(FILE_NAME)
    print(text)


    