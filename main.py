import qrcode
img = qrcode.make('Some data here')
img.save("Some_file.png")
