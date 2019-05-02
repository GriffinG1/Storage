import subprocess
import sys
import os
try:
    import qrcode
except:
    install("qrcode[pil]")
    
def install(package): # https://stackoverflow.com/a/50255019
    subprocess.call([sys.executable, "-m", "pip", "install", package])

another_code = "yes"

while not another_code == "no":
    site = input("What site do you want to make into a QR code? ")
    while not site:
        site = input("What site do you want to make into a QR code? ")
    name = input("What do you want to name the file? ")
    while not name:
        name = input("What do you want to name the file? ")

    qr = qrcode.QRCode(version=None)
    qr.add_data(site)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    if not os.path.exists("generated_qrs/"):
        os.mkdir("generated_qrs/")
    img.save(f"generated_qrs/{name}.png", format='PNG')
    print(f"Generated QR to 'generated_qrs/{name}.png'.")
    another_code = input("Do you want to generate another QR code? ")

input("Press Enter to exit.")
raise SystemExit()