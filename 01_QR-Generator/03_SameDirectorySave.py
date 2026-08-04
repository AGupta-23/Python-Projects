import qrcode as qr
import os

img = qr.make("https://www.linkedin.com/in/abhidha-gupta-822625290/")

file_path = os.path.abspath(__file__)
print(file_path)

directory_path = os.path.dirname(file_path)
print(directory_path)

loc = os.path.join(directory_path, "LinkedIn_with_os.png")

img.save(loc)  # type: ignore