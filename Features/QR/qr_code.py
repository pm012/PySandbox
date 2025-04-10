import qrcode
import os


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "qrcode1.png")    

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("Саша і Данило - друзі навік")
    qr.make(fit=True)

    # need to install pillow (PIL): pip install pillow
    img = qr.make_image(fill_color="blue", back_color="yellow")
    img.save(file_path)