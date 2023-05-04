import qrcode
import io
import os

def generate_qr(shared_secret_key,issuer, email):
    """
    Generates a QR image with the information requested by
    public 2fA autenthicator as Microsoft, Google
    PARAMETERS
        shared_secret_key:bytes string secret key over which to construct OTP
        issuer           :Hold the account's name holder
        mail             :Hold email for account holder 
    RETURNS
        Image in format png
    """
    chunk1 = "otpauth://totp/"
    chunk2 = issuer.upper()+ ":"
    chunk3 = email + "?"
    chunk4 = "secret=" + shared_secret_key + "&"
    chunk5 = "issuer=" + issuer.upper()
    qr_data = chunk1 + chunk2 + chunk3 + chunk4 + chunk5
    print(qr_data)
    img = qrcode.make(qr_data,)
    # Saving as an image file
    img.save('MyQRCode1.png')
    cwd = os.getcwd()
    imagepath= os.path.join(cwd,'MyQRCode1.png' )
    """
    f = io.StringIO()  # file to read the image
 


    qr = qrcode.QRCode()
    qr.add_data(qr_data)
    qr.print_ascii(out=f)
    f.seek(0)
    # print(f.read()) # to see it on the screen
    img = f.read()
    print(type(img))
    """
    return imagepath

generate_qr("FNKUG3TUNRITOMKUMFREK3KDG5FGQNZP", "SHIELD","philcoulson@mobilefish.com")


