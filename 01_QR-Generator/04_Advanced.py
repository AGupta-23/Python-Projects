import qrcode
from PIL import Image
import os

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H, # type: ignore
                   box_size=7, border=4)


qr.add_data("https://github.com/AGupta-23/Python-Projects/tree/main/01_QR-Generator")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color="black")

file_path = os.path.abspath(__file__)
print(file_path)

directory_path = os.path.dirname(file_path)
print(directory_path)

loc = os.path.join(directory_path, "Advance-Github.png")
img.save(loc) # type: ignore
