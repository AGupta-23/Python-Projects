import qrcode as qr

img=qr.make("https://github.com/AGupta-23")
img.save(r"D:\PythonProjects\01_QR-Generator\Github.png")