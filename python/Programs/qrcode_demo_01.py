import pyqrcode
import png
from pyqrcode import QRCode

s="https://mindslingeranu1.blogspot.com"
url= pyqrcode.create(s)
url.svg("myqr.svg",scale = 8)
url.png('myqr.png',scale = 6)
