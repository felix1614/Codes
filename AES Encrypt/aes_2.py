import itertools
import random
import string
import hashlib
from functools import wraps
from Crypto.Cipher import AES
from Crypto import Random
import base64

ref = ['rzp_test_05V5GVmEduGwSk', 'oWIdCVzHvHNOgF5Lw3gKTtAH']
BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt_(f):
    @wraps(f)
    def decorated(*args):
        return f("".join(["".join(itertools.chain.from_iterable(["".join(random.choices(string.ascii_lowercase+string.ascii_uppercase+string.digits, k=5)), args[0][i]])) if i == int(len(args[0])/2) or i == 0 or i == len(args[0])-1 else args[0][i] for i in range(len(args[0]))]), args[1])
    return decorated


def decrypt(cipher_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return decrypt_(unpad(cipher.decrypt(cipher_text[16:])))


def decrypt_(key):
    key = bytes.decode(key)
    return "".join(["" if i in range(0, 0+5) or i in range(int((len(key)-5)/2), int((len(key)-5)/2)+5) or i in range((len(key)-6), (len(key)-6)+5) else key[i] for i in range(len(key))])


@encrypt_
def encrypt(plain_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    plain_text = pad(plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text))


key, sec = ref[0], ref[1]
key_ = "secret"
enc = encrypt(sec, key_)
print(sec)
print(enc)
print(decrypt(enc, key_))
