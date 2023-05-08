#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python
#!/home/luis/anaconda3/envs/42AI-lcasado-/bin/python

from cryptography.fernet import Fernet
import os
 
 
# generate a key for encryption and decryption
# You can use fernet to generate a simmetric key
# the key or use random key generator
# here I'm using fernet to generate key
 
key = Fernet.generate_key()
cifer_key_path = os.path.join(os.environ["HOME"], ".ssh/.encrypt.key" )
with open(cifer_key_path,'wb') as f:
        f.write(key)

print(f" I generated {cifer_key_path}")
print("BE AWARE THAT NOW TOTP KEY HAS TO BE RE-CYPHERED")
"""





 Instance the Fernet class with the key
 
fernet = Fernet(key)
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)

"""
secret = '6161616162626262636363636464646465656565666666666767676768686868'
secret_bytes = bytes.fromhex(secret)
pathfile = os.path.join(os.getcwd(), "ft_otp2.hex")
with open(pathfile, 'wb') as f:
        f.write(secret_bytes)

print(f" I generated {cifer_key_path}")