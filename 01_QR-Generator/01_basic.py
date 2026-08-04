import qrcode as qr

img=qr.make("https://www.linkedin.com/in/abhidha-gupta-822625290/")
img.save("LinkedIn.png")

#To save in current folder and not in parent project folder -
# Easy option but not portable-
# change to folder directory and then run the script
# cd .\01_QR-Generator
# python 01_basic.py