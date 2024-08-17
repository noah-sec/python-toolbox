# Created while participating in course: CryptoHack.org

from Crypto.Util.number import *

code = '11515195063862318899931685488813747395775516287289682636499965282714637259206269'
byte = long_to_bytes(int(code))
print(byte)

def long_to_bytes(n: int, blocksize: int | None = 0) -> bytes:
    pass
