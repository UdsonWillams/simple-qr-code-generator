import pyqrcode as pqr
#import png
import io

url = pqr.create("https://www.linkedin.com/in/udson-willams-754137197/")
with open("linkedinqrcode.png", "w") as fstream:
    url.png("linkedinqrcode.png", scale=5)
url.png("linkedinqrcode.png", scale=5)
buffer = io.BytesIO()
url.png(buffer)
