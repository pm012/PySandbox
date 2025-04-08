import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("Саша і Данило - друзі навік")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="yellow")
img.save("qrcode1.png")