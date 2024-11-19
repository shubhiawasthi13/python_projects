# QR code Genrator
# Require---------  pip install pyqrcode, pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode

print(".........WELCOME TO QR CODE GENRATOR..........")
print("==============================================")
print("Application developed by ucb")
print("Please enter URL")
w = str(input())
url = pyqrcode.create(w)
url.svg("MyQR.svg",scale=8)
url.png("MyQR.png",scale=6)
print("QR created successfully")