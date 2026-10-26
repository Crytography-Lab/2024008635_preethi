p = int(input("Enter p: "))
q = int(input("Enter q: "))
n = p * q
phi = (p - 1) * (q - 1)
e = int(input("Enter public key e: "))

d = 1
while (e * d) % phi != 1:
    d += 1

message = int(input("Enter the message: "))
encrypted = pow(message, e, n)
print("Encrypted message: ", encrypted)

decrypted = pow(encrypted, d, n)
print("Decrypted message: ", decrypted)
