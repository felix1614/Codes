import hashlib
import random


def EVP_BytesToKey(key_len, iv_len, md, salt, data, count):
    both = [[], []]
    key = bytearray([0] * key_len)
    iv = bytearray([0] * iv_len)
    both[0] = key
    both[1] = iv
    key_ix = 0
    iv_ix = 0
    md_buf = bytearray()
    nkey = key_len
    niv = iv_len
    global i
    i = 0
    if data is None:
        return both
    addmd = 0
    while True:
        md =hashlib.md5()
        md.update(md_buf)
        cd = [i for i in md.digest()]
        if addmd > 0:
            addmd += 1
            md.update(md_buf)
        md.update(data)
        if salt is not None:
            md.update(salt)
        md_buf = md.digest()
        i = 1
        for i in range(1, count):
            # reset the digest
            md = hashlib.md5()
            md.update(md_buf)
            ef = [k for k in md.digest()]
            md_buf = md.digest()
        i = 0
        if nkey > 0:
            while True:
                if nkey == 0:
                    break
                if i == len(md_buf):
                    break
                key[key_ix] = md_buf[i]
                key_ix += 1
                nkey -= 1
                i += 1
        if niv > 0 and i != len(md_buf):
            while True:
                if niv == 0:
                    break
                if i == len(md_buf):
                    break
                iv[iv_ix] = md_buf[i]
                iv_ix += 1
                niv -= 1
                i += 1
        if nkey == 0 and niv == 0:
            break
    md_buf = bytearray(md_buf)
    for i in range(len(md_buf)):
        md_buf[i] = 0
    return both


slt = bytearray({1, 2, 3, 4, 5, 6, 7, 8})
pwd = "secretkey12345*".encode()
# cde = [list(map(ord, "12345678")), list(map(ord, "secretkey12345*"))]
md5 = hashlib.md5()
# cd = EVP_BytesToKey(int(256 / 8), 16, md5, slt, pwd, 5)
# df =[[i for i in cd[0]],[i for i in cd[1]]]
# print(cd, len(cd), len(cd[0]), len(cd[1]))


# def twoBytes(na):
#     return na % 256
# gf = [64, 42, -88, 111, -127, 105, 32, -116, -128, 85, -48, -111, 76, -84, 96, 106, 103, -6, -42, 113, 108, -113, -111, 127, 42, 77, -46, 101, 127, 16, -16, -121, -79, 75, 113, -14, -109, 103, 110, -20, -120, 124, -26, 103, -128, 123, 113, 119, 40, -121, -42, -92, 16, -120, 12, -98, -54, 61, -61, -88, -25, -119, 27, 13, -7, -79, 32, 62, 55, -102, -35, 22, -8, 19, -59, -82, -5, -42, -83, -3]
gf = [-85, -16, 2, -108, -7, -35, -41, -38, 27, 34, 39, 56, -24, 42, 77, 53, -101, -91, -128, -79, 7, -84, -99, 95, -62, -78, 115, 99, 56, -111, -37, 104]
# result = bytes(map(twoBytes, gf))
# efe = result


def hexToString(msg):
    lend = len(msg)
    data = bytearray([0] * int(lend/2))
    for i in range(0, lend, 2):
        data[int(i/2)] = (int(msg[i], 16) << 4) + int(msg[i + 1], 16)
    return data


dta = "402AA86F8169208C8055D0914CAC606A67FAD6716C8F917F2A4DD2657F10F087B14B71F293676EEC887CE667807B71772887D6A410880C9ECA3DC3A8E7891B0DF9B1203E379ADD16F813C5AEFBD6ADFD"
cd = hexToString(dta)






