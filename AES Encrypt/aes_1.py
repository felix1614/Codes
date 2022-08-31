import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(plain_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    plain_text = pad(plain_text)
    print("After padding:", plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text))


def decrypt(cipher_text, key):
    private_key = hashlib.sha256(key.encode("utf-8")).digest()
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(cipher_text[16:]))


# with open("aes_2.py", "r") as txt:
#     mes = txt.read()
#     txt.close()

message = input("enter: ")
key_ = "Hello"
encrypted_msg = encrypt(message, key_)
print("Encrypted Message:", encrypted_msg)
decrypted_msg = decrypt(encrypted_msg, key_)
dssd = bytes.decode(decrypted_msg)
print("Decrypted Message:", bytes.decode(decrypted_msg))