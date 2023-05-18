#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python3
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

import os
import datetime

# save file helper  
def save_file(filename, content):  
   f = open(filename, "wb")  
   f.write(content) 
   f.close()  


t = datetime.datetime.now()
stamp= f"{t.year:4d}{t.month:0>2}{t.day:0>2}_{t.hour}{t.minute}{t.second}"
# 2015 5 6 8 53 40


homedir = os.environ['HOME']
for keylength in range(16, 100):

##########################GENERATE CERTIFICATE PAIR########################

new_key = RSA.generate(2048)