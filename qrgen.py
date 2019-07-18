""" qrgen.py - Simple qr generator. Generates qr files to generated_qrs/
    Copyright (C) 2019  GriffinG1

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published
    by the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>."""

import subprocess
import sys
import os
try:
    import qrcode
except:
    print("Failed to load qrcode. Installing...")
    install("qrcode[pil]")
    print("qrcode successfully installed.")
    import qrcode


def install(package):  # https://stackoverflow.com/a/50255019
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
