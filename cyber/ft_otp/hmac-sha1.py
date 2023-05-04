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

# H is assumed to be a cryptographic hash function where data 
# is hashed by iterating a basic compression    function on 
# blocks of data
# B is the byte-length of blocks compressed by Hash fucntion

B = 64

# we denotes dy L the byte-lenght of hash outputs
# L = 15  #  for MD5

L = 20  #  for SHA-1

#
# the length of the secret key is up to B
# the minimal lenght for the secret is L
# when secr keys longer  than B bytes will first hash the key 
# using H and then use the resultant L byte string as the actual 
# key to HMAC

# We define two fixed and different strings ipad and opad as follows
#   (the 'i' and 'o' are mnemonics for inner and outer):
#
# ipad = the byte 0x36 repeated B times
# opad = the byte 0x5C repeated B times.

inner_pad = b'\0x36' * B
outter_pad = b'\0x5C' * B

inner_pad_big_endian = int.from_bytes(inner_pad, byteorder="big")
outter_pad_big_endian = int.from_bytes(outter_pad, byteorder="big")


text = "Hi There"
# To compute HMAC over the data `text' we perform
#      H(K XOR opad, H(K XOR ipad, text))
#        ----v-----    -----v----
#        hash_key_2    hash_key_1    

from shared_secret_key import generate_secret_key

K = generate_secret_key(len=L)
K_len = len(K)
print(len(K), " K ",K)
#   Namely,
#
#    (1) append zeros to the end of K to create a B byte string
#        (e.g., if K is of length 20 bytes and B=64, then K will be
#         appended with 44 zero bytes 0x00)
 
for _ in range(K_len,B):
    K = K + b'0'

print(len(K), " K ",K)
#    (2) XOR (bitwise exclusive-OR) the B byte string computed in step
#        (1) with ipad
K_big_endian = int.from_bytes(K, byteorder="big")
                             
hash_key_1_big_endian = K_big_endian ^ inner_pad_big_endian
print("len K ", len(K))
print("len ipad ", len(inner_pad))
hash_key_1_big_endian_len = max (len(K), len(inner_pad))
hash_key_1 = hash_key_1_big_endian.to_bytes(hash_key_1_big_endian_len, byteorder="big")
#    (3) append the stream of data 'text' to the B byte string resulting
#        from step (2)
block_to_hash = hash_key_1 + text
#    (4) apply H to the stream generated in step (3)
#    (5) XOR (bitwise exclusive-OR) the B byte string computed in
#        step (1) with opad
#    (6) append the H result from step (4) to the B byte string
#        resulting from step (5)
#    (7) apply H to the stream generated in step (6) and output
#        the result