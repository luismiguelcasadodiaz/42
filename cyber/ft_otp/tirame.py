def hexrep(hexstr, times):
    result = '0x'
    for _ in range(times):
        result = result + hexstr[2:]

myhex = b'0xA'
print("str = ",myhex)
print("hex = ",myhex.decode())
print("dec = ",int(myhex, base=16))
print("bin = ",bin(int(myhex, base=16)))
repeatedhex = hexrep(myhex,2)

