#!/usr/local/bin/python3

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import os
import datetime

def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

def egcd(a,b):
    """
    Extended euclidean ALgorithm
    """
    if a == 0:
        return(b, 0, 1)
    g, y, x = egcd(b%a, a)
    return (g, x - (b//a) * y , y)

def modinv(a,m):
    g, x, y = egcd(a,m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

plaintext = "42Barcelona"

homedir = os.environ['HOME']
pathfactors = os.path.join(homedir, "Documents/42/cyber/corsair/common_factors.txt")



with open(pathfactors,'r') as f:
    for line in f:
        factor, key_list = line.strip().split(":")
        for e in eval(key_list):  # eval cause i read str
            print(f"p_q_{e[0]:0>3} - p_q_{e[1]:0>3}")
            # import public key for which p was found
            stamp =  f"p_q_{e[0]:0>3}"
            fileNamePub = stamp + "_public.pem"
            pathPub = os.path.join(homedir, ".ssh", fileNamePub)
            with open(pathPub,'rb') as publicfile:
                publickey = RSA.import_key(publicfile.read())

            # Construct private key
            p = int(factor)
            n = publickey.n
            e = publickey.e
            q = n // p
            try:
                T = (p - 1)*(q - 1)
                d = modinv(e, T)
            except:
                d = None
            rsa_components = (n,e,d,p,q)
            privatekey= rsa_key= RSA.construct(rsa_components,consistency_check=True)
            fake_private_key = privatekey.exportKey(format='PEM',pkcs=1)
          
            # open ciphered text with the publi key
            fileNameEnc = stamp + "_message.enc"
            pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)
            with open(pathEnc, 'rb') as f:
                ciphertext=f.read()

            # create an encrypter    
            cipher = PKCS1_OAEP.new(fake_private_key)

            plaintext = cipher.decrypt(ciphertext)
            print(plaintext)





theqspathfile = os.path.join(homedir, "Documents/42/cyber/corsair/theqs.txt")
theqs=[]
with open(theqspathfile,'r') as f:
   for line in f:
      theqs.append(int(line.strip()))
print(f"len {len(theqs)}")

for num in range(len(theqs)):
    stamp =  f"p_q_{num:0>3}"
    fileNamePub = stamp + "_public.pem"
    fileNameEnc = stamp + "_message.enc"

    pathPub = os.path.join(homedir, ".ssh", fileNamePub)
    pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)

    # reading public key
    with open(pathPub,'r') as publicfile:
        publickey = RSA.import_key(publicfile.read())
        #print(publickey.n)
    
    # create an encrypter    
    cipher = PKCS1_OAEP.new(publickey)

    ciphertext = cipher.encrypt(plaintext.encode())

    
    