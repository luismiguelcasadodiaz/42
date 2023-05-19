#!/usr/local/bin/python3

import os
import rsa
import time

homedir = os.environ['HOME']
plaintext = "42Barcelona"
keylength=170  # I choose this length as it is the minimun to encrypt 42Barcelona

plaintext = "4"
keylength=90  # I choose this length as it is the minimun to encrypt 42Barcelona

for num in range(100):  #  i generate 100 keys to play with them

    stamp =  f"{keylength:0>3}_{num:0>3}"
    fileNamePub = stamp + "_public.pem"
    fileNamePri = stamp + "_private.pem"
    fileNameEnc = stamp + "_message.enc"

    pathPub = os.path.join(homedir, ".ssh", fileNamePub)
    pathPri = os.path.join(homedir, ".ssh", fileNamePri)
    pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)

    # Key generation
    (publickey, privateKey) = rsa.newkeys(keylength)

    # saving keys
    pubkeypem= publickey.save_pkcs1('PEM')
    prikeypem= privateKey.save_pkcs1('PEM')

    with open(pathPri,'wb') as f:
        f.write(prikeypem)
    with open(pathPub,'wb') as f:
        f.write(pubkeypem)

    # reading public key

    with open(pathPub,'rb') as publicfile:
        keydata = publicfile.read()

    pubkey = rsa.PublicKey._load_pkcs1_pem(keydata)

    #print(f"Public Gey Exponent  = {pubkey.e}")
    #print(f"Public Key monule    = {pubkey.n}")


    with open(pathPri,'rb') as privatefile:
        keydata = privatefile.read()
    privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')

    #print(f"Private Gey Exponent = {privkey.e}")
    #print(f"Private Key monule   = {privkey.n}")
    
    cypheredtext = rsa.encrypt(plaintext.encode(),pubkey,)
    with open("salida_encryp.txt", 'a') as f:
        line = f"{num:0>3}-e={pubkey.e}, n={pubkey.n:>52},d={privkey.d:>52}, p={privkey.p:>28}, q={privkey.q:>25},{plaintext}==>{cypheredtext}\n"
        f.write(line)

    print(f"{num:0>3}-e={pubkey.e}, n={pubkey.n:>52},d={privkey.d:>52}, p={privkey.p:>28}, q={privkey.q:>25},{plaintext}==>{cypheredtext}")

    with open(pathEnc,'wb') as f:
        f.write(cypheredtext)

