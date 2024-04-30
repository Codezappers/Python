import qrcode

data = input('Enter the data to be stored in the QR code: ')

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white')

img.save('C:/Users/Aden/OneDrive/Desktop/Personal coding/Python/myqrcode.png')