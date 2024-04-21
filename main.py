import qrcode
import image
import os
import datetime

def get_pictures_folder():
    """path folder 'Pictures' """
    if os.name == 'nt':  # Windows
        return os.path.join(os.environ['USERPROFILE'], 'Pictures')
    elif os.name == 'posix':  # Linux/macOS
        return os.path.join(os.environ['HOME'], 'Pictures')
    else:
        # OS lain
        print("OS tidak dikenali. Masukkan path folder Pictures secara manual (enter untuk batal): ")
        return input() or None

def generate_filename():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H.%M")
    return f"qrcode {timestamp}.png"
            
def get_filename():
    while True:
        custom_name = input("Masukkan nama file (enter untuk default): ")
        if not custom_name:
            return generate_filename()

        filename = os.path.join(get_pictures_folder(), f"{custom_name}.png")
        if not os.path.exists(filename):
            return filename

        # hindari duplikat
        counter = 1
        while True:
            new_filename = os.path.join(get_pictures_folder(), f"{custom_name}_{counter}.png")
            if not os.path.exists(new_filename):
                return new_filename
            counter += 1
        
# Header
print(f"{18*"=":<20}{"QRCode GENERATOR":^16}{18*"=":>20}")

# Input link      
data = input("Masukkan Link (http/https)\t: ")
while True:
    if data.startswith("https://") or data.startswith("http://"):
        if len(data) < 10 or len(data) < 9:
            print("URL terlalu pendek!")
            data = input("Masukkan link lengkap!\t\t: ")
            continue
        break
    else:
        print("URL tidak valid! Pastikan dimulai dengan http:// atau https://")
        data = input("Masukkan link lengkap!\t\t: ")
    

# Generate qrcode
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

    print(f"QRCode generated and saved as: {filename}")
    print(56*"=")
except Exception as e:
    print(f"Error generating QR code: {e}")