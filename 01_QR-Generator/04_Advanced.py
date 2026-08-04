import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H, # type: ignore
                   box_size=10, border=10)

# qr.add_data("Abhidha Gupta")
qr.add_data("https://github.com/AGupta-23")
# qr.add_data("9098977388")
# qr.add_data("abhidha2105@gmail.com")

qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")
img.save("Advance-Github.png") # type: ignore
