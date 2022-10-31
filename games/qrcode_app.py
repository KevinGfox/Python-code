import qrcode

def generate_qrcode(text):

    qr = qrcode.QRcode(
        version = 1,
        error_correction = qrcode.constants.ERROR_correct_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimg.png")

generate_qrcode("https://kevingfox.github.io/Kevin-Portfolio/")