#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python3

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import os
import datetime
import rsa

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
theqspathfile = os.path.join(homedir, "Documents/42/cyber/corsair/theqs.txt")
theqs=[]
with open(theqspathfile,'r') as f:
   for line in f:
      theqs.append(int(line.strip()))
print(f"len {len(theqs)}")

for num in range(len(theqs)):

   stamp =  f"p_q_{num:0>3}"
   fileNamePub = stamp + "_public.pem"
   fileNamePri = stamp + "_private.pem"
   fileNameEnc = stamp + "_message.enc"

   pathPub = os.path.join(homedir, ".ssh", fileNamePub)
   pathPri = os.path.join(homedir, ".ssh", fileNamePri)
   pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)
  
   #generate a fake public key
   p = 2438593310261074657282043163376290856047222440000419075612452801035390644758889499482865075970053142986916368260984858690118496306023036284680524966770279394068431807148336577519722485636930557224182394703700065632044053829756756845734485338498233667494865837330182593896052648121623458208640331155181192046654120922889117408243
   q = theqs[num]
   n = p*q
   e = 65537
   rsa_components = (n,e)
   
   rsa_key= RSA.construct(rsa_components,consistency_check=True,)
   fake_public_key  = rsa_key.export_key(format='PEM',pkcs=1)

   # save the key
   with open(pathPub, 'wb') as f:
      f.write(fake_public_key)
   print(pathPub)
"""
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
 ##########################GENERATE CERTIFICATE PAIR########################
   #rsa_key=RSA.generate(bits=1024, e=e)
   #private_key=rsa_key.export_key(format='PEM',pkcs=1)
   #public_key=rsa_key.publickey().export_key(format='PEM',pkcs=1)
   #print("qye pasas")

"""