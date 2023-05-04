
# RFC 2104
# 3. Keys
#
#   The key for HMAC can be of any length (keys longer than B bytes are
#   first hashed using H).  However, less than L bytes is strongly
#   discouraged as it would decrease the security strength of the
#   function.  Keys longer than L bytes are acceptable but the extra
#   length would not significantly increase the function strength. (A
#   longer key may be advisable if the randomness of the key is
#   considered weak.)
#
#   Keys need to be chosen at random (or using a cryptographically strong
#   pseudo-random generator seeded with a random seed), and periodically
#   refreshed.  (Current attacks do not indicate a specific recommended
#   frequency for key changes as these attacks are practically
#   infeasible.  However, periodic key refreshment is a fundamental
#   security practice that helps against potential weaknesses of the
#   function and keys, and limits the damage of an exposed key.)

import ssl
import base64

def generate_secret_key(len=20):
    """
    Returns len cryptographically strong pseudo-random bytes
    """
    secret = ssl.RAND_bytes(len) 
    secret_b32 = base64.b32encode(secret)
    #print("Secret key b32",type(K_b32), K_b32)

    return secret_b32.lower()
"""
k_b32 = generate_secret_key()
for i in range(0,32,4):
    print(k_b32[i:i+4],end=" ")

print(generate_secret_key())
"""