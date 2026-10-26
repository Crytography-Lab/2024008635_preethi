def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

a = int(input("Enter a: "))
m = int(input("Enter m: "))
print("Inverse: ", mod_inverse(a, m))
