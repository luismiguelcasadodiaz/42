import hmac, base64, struct, hashlib, time
def get_hotp_token(secret, intervals_no):
    key = base64.b32decode(secret, True)
    print("Ejemplo key =",key)
    #print("My  key_b32 =",b'chaha0s\x066\x86\x16\x86\x13\x070chaha0s\x066\x86\x16\x86\x13\x070chaha0s')
    #decoding our key
    msg = struct.pack(">Q", intervals_no)  # > = big-endian  Q = unsigned Long long
    print("Ejemplo msg =",msg)
    #print("My      msg =",b'\x00\x00\x00\x00\x03X+\x88')
    #conversions between Python values and C structs represente
    h = hmac.new(key, msg, hashlib.sha1).digest()
    print(len(h)," h =", h)
    o = o = h[19] & 15
    #print("o =", o)
    #Generate a hash using both of these. Hashing algorithm is HMAC
    h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000     # > = big-endian  I = unsigned int
    #unpacking
    return h
def get_totp_token(secret):
    #ensuring to give the same otp for 30 seconds
    x =str(get_hotp_token(secret,intervals_no=int(time.time())//30))
    #adding 0 in the beginning till OTP has 6 digits
    while len(x)!=6:
        x+='0'
    return x
#base64 encoded key
secret = 'MNUGC2DBGBZQ===='   #  16 Bytes lenghts key
secret = 'MNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQ===='   #  64 Bytes lenghts key
aaaaaa = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'
aaaaaa = '          1         2         3         4         5         6         7         8         9         0         1         2         3'
aaaaaa = '                                                                                                              1         2         3'
print(get_totp_token(secret))