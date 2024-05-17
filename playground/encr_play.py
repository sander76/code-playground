# import binascii
# import hashlib

# sh = hashlib.sha3_256(b"hello").digest()
# print("sh hello =", binascii.hexlify(sh))
# hx = bytes.hex(sh)
# print(f"sh hello = {hx}")

from Crypto.Hash import SHA512
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes

pw = "mypassword"
salt = get_random_bytes(16)
keys = PBKDF2(pw, salt, 64, count=10000, hmac_hash_module=SHA512)

print(f"key1 {keys[:32]!r}")
print(f"key2 {keys[32:]!r}")
