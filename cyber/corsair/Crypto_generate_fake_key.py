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


   pathPub = os.path.join(homedir, ".ssh", fileNamePub)

  
   #generate a fake public key
   idx1 = random.randrange(0,24)
   idx2 = random.randrange(0,24)
   p = theps[idx1]
   q = theqs[idx2]
   n = p*q
   e = 65537
   rsa_components = (n,e)
   print(stamp)
   print(f"{idx1} p= {p}")
   print(f"{idx2} q= {q}")
   print(f"n= {n}")
   
   rsa_key= RSA.construct(rsa_components,consistency_check=True,)
   fake_public_key  = rsa_key.publickey().export_key(format='PEM',pkcs=1)

   # save the key
   with open(pathPub, 'wb') as f:
      f.write(fake_public_key)
   #print(pathPub)
