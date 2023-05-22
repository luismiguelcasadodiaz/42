#!/usr/local/bin/python3

import os
from Crypto.PublicKey import RSA

def gcd(a, b):  # Greatest Common Divisor Generator (Euclidean Algorithm)
    while b != 0:  # While remainder exists
        t = b  # Initially r[k-1]
        b = a % t  # Initially r[k] = r[k-2] mod r[k-1] (where r[k-2] is a)
        a = t  # Predecessor of remainder (b)
    return a

homedir = os.environ['HOME']
plaintext = "42Barcelona"

gcd_dict = {}
allcount=0
primescoutn=0
found = False
key1 = ()
key2 = ()
p = 0

for num in range(100):  #  i generated 100 keys to play with them
    if not found:
        stamp =  f"p_q_{num:0>3}"
        fileNamePub = stamp + "_public.pem"
        fileNamePri = stamp + "_private.pem"
        fileNameEnc = stamp + "_message.enc"

        pathPub = os.path.join(homedir, ".ssh", fileNamePub)
        pathPri = os.path.join(homedir, ".ssh", fileNamePri)
        pathEnc = os.path.join(homedir, ".ssh", fileNameEnc)

        # reading first public key

        with open(pathPub,'rb') as publicfile:
            publickey1 = RSA.import_key(publicfile.read())


        for num2 in range(100):  #  i generated 100 keys to play with them
            allcount +=1
            stamp2 =  f"p_q_{num2:0>3}"
            fileNamePub2 = stamp2 + "_public.pem"
            fileNamePri2 = stamp2 + "_private.pem"
            fileNameEnc2 = stamp2 + "_message.enc"

            pathPub2 = os.path.join(homedir, ".ssh", fileNamePub2)
            pathPri2 = os.path.join(homedir, ".ssh", fileNamePri2)
            pathEnc2 = os.path.join(homedir, ".ssh", fileNameEnc2)

            if pathPub != pathPub2:

                # reading first public key

                with open(pathPub2,'rb') as publicfile2:
                    publickey2 = RSA.import_key(publicfile2.read())

                gcd_n1_n2 = gcd(publickey1.n, publickey2.n)

                if gcd_n1_n2 != 1:
                    primescoutn +=1
                    print(f"{num:0>3}-{num2:0>3} n1={publickey1.n} n2={publickey2.n} p= {gcd_n1_n2}")
                    if gcd_n1_n2 in gcd_dict.keys():
                        gcd_dict[gcd_n1_n2].append((num, num2))
                    else:
                        gcd_dict[gcd_n1_n2] = [(num, num2)]
                    #found = True
                    #key1 = (num , publickey1.n // gcd_n1_n2)
                    #key2 = (num2 , publickey2.n // gcd_n1_n2)
                    #p = gcd_n1_n2
                    
                    #break
                else:
                    print(f"{num:0>3}-{num2:0>3} primes")
    else:
        break
                    

print(f"Allcount = {allcount}")
print(f"preimescount = {primescoutn}")
print(f"num factors {len(gcd_dict.keys())}")
for k,v in gcd_dict.items():
    print(k,v)


