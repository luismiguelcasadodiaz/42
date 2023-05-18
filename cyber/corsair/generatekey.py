#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python3
#!/home/luis/anaconda3/envs/42AI-lcasado-/bin/python

import rsa
import os
import datetime
t = datetime.datetime.now()
stamp= f"{t.year:4d}{t.month:0>2}{t.day:0>2}_{t.hour}{t.minute}{t.second}"
# 2015 5 6 8 53 40

plaintext="42 Barcelona."
homedir = os.environ['HOME']
for keylength in range(16, 100):
    stamp = f"{keylength:0>3}"
    fileNamePub =  stamp + "_public.pem"
    fileNamePri =  stamp + "_private.pem"

    pathPub = os.path.join(homedir, ".ssh", fileNamePub)
    pathPri = os.path.join(homedir, ".ssh", fileNamePri)

    (publickey, privateKey) = rsa.newkeys(keylength,True,4)

    pubkeypem= publickey.save_pkcs1('PEM')
    prikeypem= privateKey.save_pkcs1('PEM')

    with open(pathPri,'wb') as f:
        f.write(prikeypem)
    with open(pathPub,'wb') as f:
        f.write(pubkeypem)
    cypheredtext = rsa.encrypt(plaintext.encode('ascii'),publickey)
    print(pathPub)
