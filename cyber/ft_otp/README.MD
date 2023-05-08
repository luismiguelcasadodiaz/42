# TOTP
## Time-based One Time Password generator with Graphical User Interface
### Sync it With Google or Microsoft Two Factor Autenticator.


This program uses as input a file wiht an hexadecimal shared key.

The hexadecimal shared key, embeded in the QR can be used for sync with Microsoft 2F.

THe hexadecimal key at this moment 8th May 2023 is a string suitable for 

base64.b32decode(secret.decode(),True, map01='l')

the Key.hex ABCDEFGHIJKLMNOPQRSTUVWXYZ234567= is base32 alfabeth

when readed from the file we got a byte array
b'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567='

We need to check its length is a multiple of 4 and bigger than 64 Hexadecimal char
