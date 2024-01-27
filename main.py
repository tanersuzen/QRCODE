import pyqrcode

url = input("enterurl to create QR code: ")

qrcode = pyqrcode.create(url)
qrcode.svg("qrcode.png",scale=5)