p = int(input("Enter prime number p: "))
g = int(input("Enter primitive root g: "))
a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

A = pow(g, a, p)
B = pow(g, b, p)

key_A = pow(B, a, p)
key_B = pow(A, b, p)

print("Alice's public key: ", A)
print("Bob's public key: ", B)
print("Alice's shared secret key: ", key_A)
print("Bob's shared secret key: ", key_B)
