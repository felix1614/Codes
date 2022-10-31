import hashlib
from Crypto.Cipher import AES

BLOCK_SIZE = 16
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]


def encrypt(plain_text, key):
    private_key = key["key"]
    plain_text = bytearray(pad(plain_text).encode())
    iv = key["iv"]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return cipher.encrypt(plain_text)


def decrypt(cipher_text, key):
    private_key = key["key"]
    iv = key["iv"]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return cipher.decrypt(cipher_text)


# def hexToString(msg):
#     lend = len(msg)
#     data = bytearray([0] * int(lend/2))
#     for i in range(0, lend, 2):
#         data[int(i/2)] = (int(msg[i], 16) << 4) + int(msg[i + 1], 16)
#     return data


# def bytesToHex(bytes_):
#     hexArray = [*"0123456789ABCDEF"]
#     hexChars = [0] * (len(bytes_)*2)
#     for j in range(len(bytes_)):
#         v = bytes_[j] & 0xFF
#         hexChars[j*2] = hexArray[v >> 4]
#         hexChars[j * 2 + 1] = hexArray[v & 0x0F]
#     return "".join(hexChars)


def keyAndIvGenerator(key_len, iv_len, salt, data, count):
    both = {"key": bytearray([0] * key_len), "iv": bytearray([0] * iv_len)}
    key_index, iv_index, addmd = 0, 0, 0
    md_buf, nkey, niv = bytearray(), key_len, iv_len
    if data is None:
        return both
    while True:
        md = hashlib.md5()
        md.update(md_buf)
        if addmd > 0:
            addmd += 1
            md.update(md_buf)
        md.update(data)
        if salt is not None:
            md.update(salt)
        md_buf = md.digest()
        for i in range(1, count):
            md = hashlib.md5()
            md.update(md_buf)
            md_buf = md.digest()
        length = 0
        if nkey > 0:
            while True:
                if nkey == 0 or length == len(md_buf):
                    break
                both["key"][key_index] = md_buf[length]
                key_index += 1
                nkey -= 1
                length += 1
        if niv > 0 and length != len(md_buf):
            while True:
                if niv == 0 or length == len(md_buf):
                    break
                both["iv"][iv_index] = md_buf[length]
                iv_index += 1
                niv -= 1
                length += 1
        if nkey == 0 and niv == 0:
            break
    return both


# msg = "f903133e8a6a30c564ccd2255f2ae50f17078abe348fa3c50f67e7679c4836e2d8fd5a9695d4f45ade590b76be854ca0020a3a1261bbb825b45b9bd2402f52be38aa2027b7797be9f3dba5fe32b84874b8e555f56b3260b769faa5d4e2040d0a1a81ee47f224b0cde7a3210e6577f4de"
msg = "e4c84c2083e0816ec5a6e61536719fd922a48199b82aca5dbb8059a09544301d0673408d939cec7798b2eaff6a65419658fdc37f9e90f345d97afe9ded60ee4035ac681a4ca361f076b43dd8a54fb6759dd47e6360be49431bfa457f1b38fa31cd08d54f86e242d98ab1157848e60810"
# msg = "402AA86F8169208C8055D0914CAC606AD82E471DF6E87F8C1637A257813991D9BA6F04DA5D8EF151BABE393471EAB7F44435803F514DABB6C8A531F2CBC7D4E4383E1A9534C3F7C42C22AF0DD121F2161AC023AAC47D88D6B01DE5BCA93095F52B8B0111E9828F3C218AAE67CF70950AFD850792E13B53E605A4121532F7B3DD2DAA4F6A3F9BA17B4C244FC5A68EFC11763AF39961FCDCC8686755DFE46802E73164F245371AEA8FE0DC12229FCBD2981F6E5038D6EEE1926F741CB560A963313D46EAB02AF4F0C1813D82F5472142A098E862610CE6EF383F2DCBD14E6651C0"
# msg = "e4c84c2083e0816ec5a6e61536719fd922a48199b82aca5dbb8059a09544301d0673408d939cec7798b2eaff6a65419658fdc37f9e90f345d97afe9ded60ee4035ac681a4ca361f076b43dd8a54fb6759dd47e6360be49431bfa457f1b38fa31cd08d54f86e242d98ab1157848e60810"
salt = bytearray({1, 2, 3, 4, 5, 6, 7, 8})
secretKey = "secretkey12345*".encode()
keyAndIv = keyAndIvGenerator(32, 16, salt, secretKey,
                             5)  # int(256 / 8) ==> key length, 16 ==> IV length, 5 ==> Traverse count
# message = hexToString(msg)
message = bytes.fromhex(msg)
decrypted_msg = unpad(decrypt(message, keyAndIv))
df = bytes.decode(decrypted_msg)
print(eval(bytes.decode(decrypted_msg)))

#   **ENCRYPTION**
# text = json.dumps(df)
# text = str(df)
text = "{\"ApiRequest\":\"RechargeRequest\",\"Flat_Id\":\"18565\",\"Operator_Name\":\"Testing\",\"Amount_Recieved\":\"100\"}"
# text = "{'ApiRequest':'CustDetails','Flat_Id':'4','Operator_Name':'Testing'}"
# text = eval(df)
# text['Flat_Id'] = '9876'
text = str(text)
encryptMsg = encrypt(text, keyAndIv)
cdc = encryptMsg.hex()
# fdfd = bytesToHex(encryptMsg)

#  ** DECRYPTION**
# messagess = hexToString(cdc)
messagess = bytes.fromhex(cdc)
decrypted_msg = unpad(decrypt(messagess, keyAndIv))
cdsc = eval(bytes.decode(decrypted_msg))
print(cdsc)

