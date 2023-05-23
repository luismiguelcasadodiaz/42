#!/usr/local/bin/python3

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import os
import datetime
import random

# save file helper  
def save_file(filename, content):  
   f = open(filename, "wb")  
   f.write(content) 
   f.close()  


t = datetime.datetime.now()
stamp= f"{t.year:4d}{t.month:0>2}{t.day:0>2}_{t.hour}{t.minute}{t.second}"
# 2015 5 6 8 53 40

plaintext = "Barcelona"

homedir = os.environ['HOME']

# Read the ps
theqspathfile = os.path.join(homedir, "Documents/42/cyber/corsair/theqs.txt")
theqs=[]
with open(theqspathfile,'r') as f:
   for line in f:
      theqs.append(int(line.strip()))
print(f"qs len {len(theqs)}")

# read the qs
thepspathfile = os.path.join(homedir, "Documents/42/cyber/corsair/theps.txt")
theps=[]
with open(thepspathfile,'r') as f:
   for line in f:
      theps.append(int(line.strip()))
print(f"Ps len {len(theqs)}")

for num in range(len(theqs)):

   stamp =  f"p_q_{num:0>3}"
   fileNamePub = stamp + "_public.pem"
   fileNamePri = stamp + "_private.pem"
   fileNameEnc = stamp + "_message.enc"

   pathPub = os.path.join(homedir, ".ssh", fileNamePub)
   pathPri = os.path.join(homedir, ".ssh", fileNamePri)
   pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)
  
   #generate a fake public key
   idx = random.randrange(0,12)
   p = theps[idx]
   q = theqs[idx]
   n = p*q
   e = 65537
   rsa_components = (n,e)
   
   rsa_key= RSA.construct(rsa_components,consistency_check=True,)
   fake_public_key  = rsa_key.export_key(format='PEM',pkcs=1)

   # save the key
   with open(pathPub, 'wb') as f:
      f.write(fake_public_key)
   print(pathPub)

   # reading public key

   with open(pathPub,'r') as publicfile:
        keydata = publicfile.read().strip()

   pubkey = rsa.PublicKey.load_pkcs1(keydata)
   cypheredtext = rsa.encrypt(plaintext.encode(),pubkey,)
   
   with open(pathEnc,'wb') as f:
        f.write(cypheredtext)
   #cypheredtext = RSA.
   #.encrypt(plaintext.encode(),fake_public_key,)
   with open("salida_crypto.txt", 'a') as f:
      line = f"{num:0>3}-e={pubkey.e}, n={pubkey.n:>52},d={rsa_key.d:>52}, p={rsa_key.p:>28}, q={rsa_key.q:>25},{plaintext}==>{cypheredtext}\n"
      f.write(line)

   print(f"{num:0>3}-e={rsa_key.e}, n={rsa_key.n:>52},d={rsa_key.d:>52}, p={rsa_key.p:>28}, q={rsa_key.q:>25},{plaintext}==>{cypheredtext}")

   with open(pathEnc,'wb') as f:
        f.write(cypheredtext)
