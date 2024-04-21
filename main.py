import qrcode
import image
import os

def get_pictures_folder():
    """Mendapatkan path folder 'Pictures'"""
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Pictures')
    elif os.name == 'posix':  # Linux/macOS
        return os.path.join(os.environ['HOME'], 'Pictures')
    else:
        # OS lain
        print("Sistem operasi tidak dikenali. Masukkan path folder Pictures secara manual (kosong untuk batal): ")
        return input() or None  # Kosong untuk batal

def generate_filename():
    counter = 0
    while True:
        filename = f"qrcode_{counter}.png"
        if not os.path.exists(filename):
            return filename
        counter += 1

def get_filename():
    while True:
        custom_name = input("Masukkan nama file (enter untuk default): ")
        if custom_name:
            return f"{custom_name}.png"
        else:
            return generate_filename()
        
# HEADER
print(f"{10*"*":<12}{"QRCode GENERATOR":^16}{10*"*":>12}")

# Input link      
data = input("Masukkan Link: ")
while True:
    if data.startswith("https://") or data.startswith("http://"):
        break
    else:
        data = input("Masukkan link lengkap!: ")
        continue
    

# generate qrcode
try:
    qr = qrcode.QRCode(
        version=5,  # semakin besar semakin ruwet(banyak kotak)
        box_size=10,  # ukuran tampilan
        border=5,  # border
    )

    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    filename = os.path.join(get_pictures_folder(), get_filename())
    img.save(filename)

    print(f"QRCode generated and saved as: \033[32m{filename}\033[0m") # warna hijau
    print(f"{40*"*"}")
except Exception as e:
    print(f"Error generating QR code: {e}")