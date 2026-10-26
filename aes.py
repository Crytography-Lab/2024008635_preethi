from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'1234567890123456'
message = input("Enter plaintext: ").encode()

cipher = AES.new(key, AES.MODE_ECB)
encrypted = cipher.encrypt(pad(message, AES.block_size))
print("Encrypted: ", encrypted)

decipher = AES.new(key, AES.MODE_ECB)
decrypted = unpad(decipher.decrypt(encrypted), AES.block_size)
print("Decrypted: ", decrypted.decode())
