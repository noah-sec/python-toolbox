# From CryptoHack.org course
import base64

code = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
byte = bytes.fromhex(code)
b64 = base64.b64encode(byte)
print(b64)