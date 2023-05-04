import qrcode

def generate_qr(shared_secret_key,domain_name, email):
    shared_secret_key
    data = shared_secret_key
    img = qrcode.make(data)
 
    # Saving as an image file
    img.save('MyQRCode1.png')
