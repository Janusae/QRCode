import qrcode

try:
    url = input("Inter your url>")
    qr = qrcode.make(url)
    output_File = "QRCODE.png"
    qr.save(output_File)
    print(f"We created a image({output_File}) for you!")
except :
    print("We have an issue!")
