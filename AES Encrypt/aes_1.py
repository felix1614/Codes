import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(plain_text, key):
    private_key = hashlib.md5(key.encode("utf-8")).digest()
    plain_text = pad(plain_text)
    print("After padding:", plain_text)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(plain_text.encode("utf-8")))


def decrypt(cipher_text, key):
    private_key = hashlib.md5(key.encode("utf-8")).digest()
    cipher_text = base64.b64decode(cipher_text)
    iv = cipher_text[:16]
    cipher_text_fin = cipher_text[16:]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    df = cipher.decrypt(cipher_text_fin)
    return unpad(cipher.decrypt(cipher_text_fin))


# message = input("enter: ")
key_ = "secretkey12345*"
# message = "402AA86F8169208C8055D0914CAC606A67FAD6716C8F917F2A4DD2657F10F087B14B71F293676EEC887CE667807B71772887D6A410880C9ECA3DC3A8E7891B0DF9B1203E379ADD16F813C5AEFBD6ADFD"
encrypted_msg = "402AA86F8169208C8055D0914CAC606A67FAD6716C8F917F2A4DD2657F10F087B14B71F293676EEC887CE667807B71772887D6A410880C9ECA3DC3A8E7891B0DF9B1203E379ADD16F813C5AEFBD6ADFD"
# encrypted_msg = encrypt(message, key_)
print("Encrypted Message:", encrypted_msg)
decrypted_msg = decrypt(encrypted_msg, key_)
dssd = bytes.decode(decrypted_msg)
print("Decrypted Message:", bytes.decode(decrypted_msg.encode("utf-8")))