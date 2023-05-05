# RFC 2104
# Message Authentication
# MAC stands for "Message Autentication Codes"
# MAC to be used between two parties that uses a secret for 
# HMAC the H denotes a Hash function
# HMAC-SHA1 uses SHA-1 as hash method
# HMAC-MD5 uses MD5 as hash method
#
# HMAC requires a H function and a secret key K
#
from  hashlib import md5 as H

import base64, struct, time


params = {'openssl_md5': {'B': 64, 'L':16},
          'openssl_sha1':{'B': 64, 'L':20}
          }
# H is assumed to be a cryptographic hash function where data 
# is hashed by iterating a basic compression    function on 
# blocks of data
# B is the byte-length of blocks compressed by Hash fucntion
#B = 64  #  for MD5
B = params[H.__name__]['B']   # bytes
#B = 64  #  for SHA-1
# we denotes dy L the byte-lenght of hash outputs
#L = 15  #  for MD5
L = params[H.__name__]['L']   # bytes
#L = 20  #  for SHA-1

#
# the length in bytes of the secret key is up to B
# the minimal lenght in bytes for the secret is L
# when secr keys longer  than B bytes will first hash the key 
# using H and then use the resultant L byte string as the actual 
# key to HMAC

# We define two fixed and different strings ipad and opad as follows
#   (the 'i' and 'o' are mnemonics for inner and outer):
#
# ipad = the byte 0x36 repeated B times
# opad = the byte 0x5C repeated B times.


"""
trans_5C = bytes((x ^ 0x5C) for x in range(256))
trans_36 = bytes((x ^ 0x36) for x in range(256))
"""

i_pad = 0x36      # 0x36 = 54
o_pad = 0x5C     # 0x5C = 92
inner_pad = 0x0
outter_pad = 0x0
for _ in range(B-1):
    inner_pad = (inner_pad << 8) + i_pad
    outter_pad = (outter_pad << 8) + o_pad
"""    
print(len(hex(inner_pad)),"Inner_pad  hex", hex(inner_pad))
print("    Inner_pad  dec", inner_pad)
print(len(hex(outter_pad)), "Outter_pad hex", hex(outter_pad))
print("    Outter_pad dec", outter_pad)
"""

#BYTEORDER = "little"
BYTEORDER = "big"
#inner_pad_big_endian = int.from_bytes(inner_pad, byteorder=BYTEORDER)
#outter_pad_big_endian = int.from_bytes(outter_pad, byteorder=BYTEORDER)
inner_pad_big_endian = inner_pad
outter_pad_big_endian = outter_pad

text = b'what do ya want for nothing?'
text = struct.pack(">Q", int(time.time())//30)

print(len(text), "msg       = ", text)

#from shared_secret_key import generate_secret_key

#K = generate_secret_key(len=L)

# I USE THIS KEY FROM AN TOTP LIBRARY FOR TEXT
K = 'MNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQMNUGC2DBGBZQ'
K_len = len(str(K))
#print(len(str(K)), " Key_len ",K)

# To compute HMAC over the data `text' we perform
#      H(K XOR opad, H(K XOR ipad, text))
#        ----v-----    -----v----
#        hash_key_2    hash_key_1    


#   Namely,
#
#    (1) append zeros to the end of K to create a B byte string
#        (e.g., if K is of length 20 bytes and B=64, then K will be
#         appended with 44 zero bytes 0x00)
 
for _ in range(K_len,B):
    K = K + "="

#print(len(K), " Key_pad ",K)
K_b = K.encode()
#print(len(K_b), " Key_bst ",K_b)
K_b32 = base64.b32decode(K_b, True)
print(len(K_b32), " Key_b32 =",K_b32)

#    (2) XOR (bitwise exclusive-OR) the B byte string computed in step
#        (1) with ipad
K_b32_big_endian = int.from_bytes(K_b32, byteorder=BYTEORDER)
print(len(str(K_b32_big_endian)),"K_b32_big_endian ",K_b32_big_endian)                             
hash_key_1_big_endian = K_b32_big_endian ^ inner_pad_big_endian


hash_key_1_big_endian_len = max (len(K_b32), len(hex(inner_pad)))
hash_key_1 = hash_key_1_big_endian.to_bytes(hash_key_1_big_endian_len, byteorder=BYTEORDER)
#    (3) append the stream of data 'text' to the B byte string resulting
#        from step (2)
block_to_hash_1 = hash_key_1 + text
#    (4) apply H to the stream generated in step (3)
hashed_block_1 = H(block_to_hash_1).digest()
#    (5) XOR (bitwise exclusive-OR) the B byte string computed in
#        step (1) with opad
hash_key_2_big_endian = K_b32_big_endian ^ outter_pad_big_endian

hash_key_2_big_endian_len = max (len(K_b32), len(hex(inner_pad)))
hash_key_2 = hash_key_2_big_endian.to_bytes(hash_key_2_big_endian_len, byteorder=BYTEORDER)
#    (6) append the H result from step (4) to the B byte string
#        resulting from step (5)
block_to_hash_2 = hashed_block_1 + hash_key_2
#    (7) apply H to the stream generated in step (6) and output
#        the result
hashed_block_2 = H(block_to_hash_2).digest()
print(len(hashed_block_2)," h = ",hashed_block_2)
print(int.from_bytes(hashed_block_2, byteorder=BYTEORDER))
print(0x750c783e6ab0b503eaa86e310a5db738)
import hmac
h = hmac.new(b'Jefe', text, H).digest()
print(int.from_bytes(h, byteorder=BYTEORDER))

print("key = b'chaha0s\x066\x86\x16\x86\x13\x070chaha0s\x066\x86\x16\x86\x13\x070chaha0s'")
print("msg = b'\x00\x00\x00\x00\x03X*\xcc'")
print("h = b'\x13\xb1-\xe5\x8f\xe8\xa3\xa5\xc09\xe8D>\x0eK\xaaQ\x13I\x06'")