from Crypto.Cipher import DES

key = b'8bytekey'
plaintext = input("Enter 8 characters: ").encode()
if len(plaintext) != 8:
    print("Plaintext must be exactly 8 bytes")
else:
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)
    print("Encrypted text: ", ciphertext.hex())
    
    decipher = DES.new(key, DES.MODE_ECB)
    decrypted = decipher.decrypt(ciphertext)
    print("Decrypted text: ", decrypted.decode())
