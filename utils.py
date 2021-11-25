import math
import hashlib
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def genSecret(v):
	sha256 = hashlib.sha256()
	sha256.update(v.to_bytes(length=math.ceil((v.bit_length()+1) / 8), byteorder='big', signed=True))
	return sha256.digest()[:16]

def decrypt(hex_enc_msg, secret):
	msg_bytes = bytes.fromhex(hex_enc_msg)
	iv = msg_bytes[:16]
	enc_message = msg_bytes[16:]
	aes = AES.new(bytes.fromhex(secret), AES.MODE_CBC, iv)
	clear_msg = unpad(aes.decrypt(enc_message),AES.block_size).decode('utf-8').strip()
	return str(clear_msg)

def reverse(msg):
	rev = msg[::-1].encode('utf-8')
	return rev

def encrypt(clear_message, secret):
	msg_bytes = bytes(clear_message)
	msg_bytes = pad(msg_bytes, AES.block_size)
	iv = urandom(16)
	aes = AES.new(bytes.fromhex(secret), AES.MODE_CBC, iv)
	ciphered_msg = aes.encrypt(msg_bytes)
	return iv.hex() + ciphered_msg.hex()
        