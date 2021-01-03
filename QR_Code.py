# pip install pyqrcode
# pip install pypng

import os
import pyqrcode
import png
from pyqrcode import QRCode

QRstring=input("Inserisci l'URL del sito di cui vuoi il QRcode: ")   # URL del sito
url=pyqrcode.create(QRstring)
nome=input("Inserisci Il Nome del FIle QR: ")
if not os.path.isdir(r".\QRs"): #Creo la cartella Qrs se non esiste
    os.mkdir(r".\QRs")
if os.path.isdir(r".\QRs"):    #Se QRs esiste ci salvo il file png
    url.png(f".\\QRs\\{nome}.png", scale=8)