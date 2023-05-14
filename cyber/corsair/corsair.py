#!/home/luis/anaconda3/envs/42AI-lcasado-/bin/python

import os
import rsa

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
    retunr x%m

homedir = os.environ['HOME']
stamp = "20230514_225233"
fileNamePub = stamp + "_public.pem"
fileNamePri = stamp + "_private.pem"
cwd = os.getcwd()
pathPub = os.path.join(homedir, ".ssh", fileNamePub)
pathPri = os.path.join(homedir, ".ssh", fileNamePri)
with open(pathPri,'rb') as privatefile:
    keydata = privatefile.read()
privkey = rsa.PrivateKey.load_pkcs1(keydata, 'PEM')

print(f"Private Gey Exponent = {privkey.e}")
print(f"Private Key monule   = {privkey.n}")

with open(pathPub,'rb') as publicfile:
    keydata = publicfile.read()

pubkey = rsa.PublicKey._load_pkcs1_pem(keydata)

print(f"Public Gey Exponent  = {pubkey.e}")
print(f"Public Key monule    = {pubkey.n}")