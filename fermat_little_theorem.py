a = int(input("Enter a: "))
p = int(input("Enter a prime number p: "))
result = pow(a, p - 1, p)
print(f"a^(p-1) mod p = {result}")
if result == 1:
    print("Fermat's little theorem is verified.")
else:
    print("Fermat's little theorem is not verified.")
