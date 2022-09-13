#pip install python-barcode

from barcode import EAN13
from barcode.writer import ImageWriter

def generator(num):
    qr_code = EAN13(num, writer=ImageWriter())
    qr_code.save("bar_code")

if __name__ == "__main__":
    generator(input('Enter 12 Digit number to Generate Bar Code : ' ))
