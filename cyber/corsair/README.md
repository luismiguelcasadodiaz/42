# corsair.py

After studing RSA mathematics i learnt that is mathemattically possible obtaing a private key
from a public key.

given p & q positive big primes

being e (exponent) = 65537 and n (modulus) = p * q 

n is the open secret (Ellis - 1970)

encryption : C = pow(M,e) mod n   
decryption : M = pow(C,d) mod n

From public key we con go to private key with this formula
d * e congruent wiht 1 * (mod λ(n))

d is de **modular multiplier inverse** of e and λ(n)

```
def modinv(a,m):
    g, x, y = egcd(a,m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m
```
λ(n) is the Carmichael totien function

```
def carmichael(n):
    coprimes = [x for x in range(1, n) if gcd(x, n) == 1]
    k = 1
    while not all(pow(x, k, n) == 1 for x in coprimes):
        k += 1
    return k
```

egcd is the  extended euclidean algoritm. this algorithm, aside calculate
the gcd thru the remainders of the division, it takes into consiseration
the quiotiens of such division.

```
def egcd(a,b):
    """
    Extended euclidean ALgorithm
    """
    if a == 0:
        return(b, 0, 1)
    g, y, x = egcd(b%a, a)
    return (g, x - (b//a) * y , y)
```

Althoug it is mathematically possible to infer private key from public key, computationally
is not possible nowadays.

I timeit the algorithm with these results


|len(n)  |(secs)| n            | e   |λ(n)     |d
|--------|------|:------------:|-----|---------|-----
| 16 bits|  000 |  n=0000055189|65537| 4560    | 833|
| 17 bits|  000 |  n=0000049163|65537| 24360   | 19913|
| 18 bits|  000 |  n=0000166493|65537| 82830   | 28643|
| 19 bits|  000 |  n=0000142859|65537| 71052   | 2873|
| 20 bits|  003 |  n=0000711197|65537| 354750  | 276473|
| 21 bits|  001 |  n=0000637253|65537| 45402   | 21719|
| 22 bits|  012 |  n=0003330841|65537| 831796  | 394861|
| 23 bits|  007 |  n=0002630651|65537| 262740  | 192173|
| 24 bits|  030 |  n=0009554689|65537| 367250  | 135223|
| 25 bits|  045 |  n=0009027989|65537| 4510950 | 2032223|
| 26 bits|  195 |  n=0050975047|65537| 8493456 | 8041937 |
| 27 bits|  142 |  n=0038412643|65537| 6400008 | 4579721 |
| 28 bits|  793 |  n=0178359197|65537| 44583120| 32650433|
| 29 bits|  993 |  n=0178371139|65537| 89172212| 31403553|
| 30 bits| 2628 |  n=0573445219|65537| 95566020| 45780173|
| 31 bits| 2690 |  n=0615414277|65537| 51280368| 37485521|
|512 bits| ???? |  n=10198396198775561957312427155980896031621481057689583114412695093823692869122007487913250993135767612909846550167087384856500083695811014490975969639561161|65537|?|?|


all this you can find it in corsair.py

# openssl_generate_key.py & rsa_generate_key.py

I need different approach.

I need pairs of keys with open secret that have common factors. This is only possible if the
rsa random generator is weak woht low entropy.

It is quite relevant to me that imported library matters.

Working in corsair 42 Barcelona cybersecyrity bootcamp Challenge I uncovered that
```
import rsa
(publickey, privateKey)  rsa.newkeys(keylength,True,4)  

```

allows keylenght starting in 16 Bits, but 

```
from cryptography.hazmat.primitives.asymmetric import rsa 

private_key = rsa.generate_private_key(  
    public_exponent=65537,  
    key_size=keylength,  
    backend=default_backend()  
)

```

raises ValueError: key_size must be at least 512-bits.

Additionally i uncover that 

```
import rsa
plaintext="4"
(publickey, privateKey) = rsa.newkeys(keylength,True,4)
cypheredtext = rsa.encrypt(plaintext.encode('ascii'),publickey)
```

works with keylenght >= 90 bits

if we add one more letter to the plaintext

```
import rsa
plaintext="42"
(publickey, privateKey) = rsa.newkeys(keylength,True,4)
cypheredtext = rsa.encrypt(plaintext.encode('ascii'),publickey)
```

works with keylenght >= 98 bits




|To encryp      |keylenght >=  |-----BEGIN RSA PUBLIC KEY-----
|---------      |:-----------: |--------------------------------------------
|"4"            |>=  90 bits   |MBMCDAOPHm2kz6tYv+tCCwIDAQAB
|"42"           |>=  98 bits   |MBQCDQLdTVvzDOKJQOOcQL0CAwEAAQ==
|"42B"          |>= 106 bits   |MBUCDgL+FzV3A+pDocXNCmMpAgMBAAE=
|"42Ba"         |>= 114 bits   |MBYCDwIQZLre60pgkhdw3DbZ6QIDAQAB
|"42Bar"        |>= 122 bits   |MBcCEAMS0QDTwtxLRpZJcGvhCxkCAwEAAQ==
|"42Barc"       |>= 130 bits   |MBgCEQIny18a4Vn/LCGRgZBf9cRHAgMBAAE=
|"42Barce"      |>= 138 bits   |MBkCEgIxB1y1LNZQIPA+sN/+P9cCkwIDAQAB
|"42Barcel"     |>= 146 bits   |MBoCEwMjAA9Q97ISXi2o2Mk3ICW2JssCAwEAAQ==
|"42Barcelo"    |>= 154 bits   |MBsCFAIaRDbXdW29NmXte7BBI07nHg4rAgMBAAE=
|"42Barcelon"   |>= 162 bits   |MBwCFQNtXHe4G4RCQwSdYhhR/EJjGRd+AwIDAQAB
|"42Barcelona"  |>= 170 bits   |MB0CFgOd9wlBGunhTRvI5GQzi+7rMOT1LR8CAwEAAQ==

According to this i will use pairs of public-private keys w a modulus of n
that fits in 170 bits.

plaintext lenght has to be no longer than k-11 bytes, being k the lenght in bytes
required to hold n

```

```

Another learning is about decoding. 
I have to encrypt a bytes array, so i encode the plaintext
I have to decode the encrypted tokes as it is.

I tryed otherwise and i got errors
```
cypheredtext = rsa.encrypt(plaintext.encode(),pubkey,)
deciferedtext = rsa.decrypt(cypheredtext,privkey)
  
```
# find_gcd.py
I generated 100 pairs of public-private RSA keys wiht a modulus(n) of length of 170 bits
After calculate 9900 gdc between all diferente 99 pairs i concluded that rsa uses a
strong primes generator, despite deal wiht 170 bits.

I repeated the experiment wiht a modulus of lenth 90 getting same results.

My final approach is generate the paisr os public and private keys using primes not generated randonlly.



