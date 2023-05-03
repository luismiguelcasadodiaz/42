#!/Users/lcasado-/miniconda3/envs/42AI-lcasado-/bin/python

import datetime
dt_000 = datetime.datetime.fromtimestamp(0)
dt_bcn = datetime.datetime.now()
dt_utc = datetime.datetime.now(datetime.timezone.utc)

print("000 ", dt_000)
print("BCN ", dt_bcn)
print("UTC ", dt_utc)
#convert UTC to unix time  1/1/1970
dt_epc = datetime.datetime.fromtimestamp(dt_utc.timestamp())
print("EPC  ", dt_epc)

print("UTC_TS", dt_utc.timestamp())
print("000_TS", dt_000.timestamp())

# Segun esto tengo que dividir dt_utc.timestamp
timestep = 30  # Seconds
N = dt_utc.timestamp() // timestep
print(N)

ejemplo = datetime.datetime(2018,12,4,12,24,00)
N = ejemplo.timestamp() // timestep
print(N)