import binascii
from crccheck.crc import Crc16Modbus

payload='0110DCBC71670004089533349400004461000042340000000000003F8000003F802400497473597596E62A00023247'
# st = time.time()
parse = payload.split('&')
hex_data =payload
# verify  crc
payload_crc = "167F"
prepared = binascii.unhexlify(str.encode(hex_data))
calculated_crc = Crc16Modbus().process(prepared).finalhex().lower()
if sorted(calculated_crc) != sorted(payload_crc):
    print('crc not matched ', calculated_crc, payload_crc)
