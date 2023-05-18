It is quite relevant to me that imported library matters.

Working in corsair 42 Barcelona cybersecyrity bootcamp Challenge I uncovered that
```import rsa
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

