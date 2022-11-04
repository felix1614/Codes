# from hashlib
import hashlib
from Crypto.Cipher import AES
from Crypto import Random
import base64



def EVP_BytesToKey(key_len=int, iv_len=int, md=None, salt=list, data=list, count=int):
		both = [[], []]
		key = []
		iv = []
		key_ix = 0
		iv_ix = 0
		both[0].extend(key)
		both[1].extend(iv)
		md_buf = None
		nkey = key_len
		niv = iv_len
		i = 0
		if data is None:
			return both
		addmd = 0
		while True:
			md.hexdigest()
			addmd+=1
			if addmd > 0:
				md.update(md_buf)
			md.update(data)
			if None != salt:
				md.update(salt, 0, 8)
			md_buf = md.digest()
			for i in range(1, count):
				md.reset()
				md.update(md_buf)
				md_buf = md.digest()
			i = 0
			if nkey > 0 :
				while True:
					if nkey == 0:
						break
					if i == len(md_buf):
						break
					key_ix+=1
					key[key_ix] = md_buf[i]
					nkey-=1
					i+=1

			if niv > 0 and i != len(md_buf):
				while True:
					if niv == 0:
						break
					if i == len(md_buf):
						break
					iv_ix+=1
					iv[iv_ix] = md_buf[i]
					niv-=1
					i+=1
			if nkey == 0 and niv == 0:
				break

		for i in range(len(md_buf)):
			md_buf[i] = 0
		return both


KEY_SIZE_BITS = 256
dat = list(map(ord, "secretkey12345*"))
md1 = hashlib.md5()
df = EVP_BytesToKey(key_len=int(KEY_SIZE_BITS/8), iv_len=16, md=md1,salt=[1,2,3,4,5,6,7,8], data=dat,count=5)


