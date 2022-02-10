# Python program to explain os.urandom() method

# importing os module
import os
import base64

# Declaring size
size = 5

# Using os.urandom() method
result = os.urandom(size)
chuyenchuoi = result.encode()

# Print the random bytes string
# Output will be different everytime
print(type(result))
print(result)
print(type(chuyenchuoi))
print(chuyenchuoi)
'''
import pickle
import hashlib
import hmac
import os
from Crypto.Cipher import AES


class AuthenticationError(Exception): pass


class Crypticle(object):
    """Authenticated encryption class

    Encryption algorithm: AES-CBC
    Signing algorithm: HMAC-SHA256
    """

    PICKLE_PAD = "pickle::"
    AES_BLOCK_SIZE = 16
    SIG_SIZE = hashlib.sha256().digest_size

    def __init__(self, key_string, key_size=192):
        self.keys = self.extract_keys(key_string, key_size)
        self.key_size = key_size

    @classmethod
    def generate_key_string(cls, key_size=192):
        key = os.urandom(int(key_size / 8) + cls.SIG_SIZE)
        return key.encode("base64").replace("\n", "")


if __name__ == "__main__":
    # usage example
    key = Crypticle.generate_key_string()
    data = {"dict": "full", "of": "secrets"}
    crypt = Crypticle(key)
    safe = crypt.dumps(data)
    assert data == crypt.loads(safe)
    print
    "encrypted data:"
    print
    safe.encode("base64")
'''