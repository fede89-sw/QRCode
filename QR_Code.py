import os
import pyqrcode
import png
from pyqrcode import QRCode

QRstring=input("Inserisci l'URL del sito di cui vuoi il QRcode: ")
url=pyqrcode.create(QRstring)
nome=input("Inserisci Il Nome del FIle QR: ")
if not os.path.isdir(r".\QRs"):
    os.mkdir(r".\QRs")
if os.path.isdir(r".\QRs"):
    url.png(f".\\QRs\\{nome}.png", scale=8)
