import pyqrcode
from PIL import Image
link=input("Enter your link: ")
qr_code=pyqrcode.create(link)
qr_code.png("QRCode.png", scale=5)
Image.open("QRCode.png")