import qrcode

img = qrcode.make("Hello World!")
img.save("my_qrcode.png")