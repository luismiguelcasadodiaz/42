#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python


# Aprendizaje:
# el tiempo zero el ordenador te lo da en la zona horaria en la que estas
# cuando le pregunt mi tiempo zero me dice que fue el 1/1/1970 a la 1:00:00
# ya que el tiempo cer de este ordenadore situado en Barcelona es ir una hora 
# por delante de Grenwich


import datetime
import pytz
import struct
tz_where_am_i = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
dt_000 = datetime.datetime.fromtimestamp(0)
dt_bcn = datetime.datetime.now()
dt_utc = datetime.datetime.now(datetime.timezone.utc)

print("000 ", dt_000)
dt_000_utc = dt_000.astimezone(pytz.timezone('UTC'))
print("BCN ", dt_bcn)
print("UTC ", dt_utc)
print("000_UTC ", dt_000_utc)
#convert UTC to unix time  1/1/1970
dt_epc = datetime.datetime.fromtimestamp(dt_utc.timestamp())
print("EPC  ", dt_epc)

print("UTC_TS", dt_utc.timestamp())
print("000_TS", dt_000.timestamp())

dt_utc = datetime.datetime.now(datetime.timezone.utc).timestamp()
print("UTC_TS", dt_utc)
print("UTC_TS", int(dt_utc))


# divido la correspondencia de mi tiempo 
#dt_vid = datetime.datetime(2018,12,4,20,24,20, tzinfo=pytz.timezone('Asia/Shanghai'))

dt_vid = datetime.datetime(2018,12,4,12,24,20, tzinfo=pytz.UTC)

dt_vid_utc = dt_vid.astimezone(pytz.UTC)
print("VID_TS", dt_vid_utc.timestamp())
timestep = 30  # Seconds
Nhex_rigth_len = 16
N = int(dt_vid.timestamp() // timestep)
print("N dec    ", N)
Nhex = hex(N)[2:]  # remove '0x'
print("N hex    ", Nhex)
Nhex_len = len(Nhex)
Nhex_16 = f"0x{Nhex:0>{Nhex_rigth_len}}"
print("N hex_16 ",Nhex_16)

msg = struct.pack(">Q", N)
print("N Bytes  ", msg)


an_integer = int(Nhex_16,Nhex_rigth_len)
print("an_integer ", an_integer)
print("an Hex", hex(an_integer))


m = bytes.fromhex(Nhex_16[2:])
print(m)
"""
Hbytes=(N).to_bytes(length=4, byteorder="big")
aux = b'\x00\x00\x00\x00\x00\x00\x00\x00'
auxb = bin(aux)
print(type(Hbytes), type(aux))
r = bin(aux) | bin(an_integer)
print("Hbytes ",  r)
print("Hbytes len ",len(Hbytes))

"""