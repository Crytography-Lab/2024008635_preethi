def mod_inverse(b, m):
    for i in range(1, m):
        if (b * i) % m == 1:
            return i
    return None

def chinese_rem(a, n):
    p = 1
    for i in range(len(n)):
        p *= n[i]
    
    x = 0
    for i in range(len(n)):
        pp = p // n[i]
        mv = mod_inverse(pp, n[i])
        x += a[i] * pp * mv
    return x % p

q = int(input("Enter the number of inputs: "))
n = []
a = []
for i in range(1, q + 1):
    n.append(int(input("Enter n: ")))
    a.append(int(input("Enter a: ")))

print("The solution is: ", chinese_rem(a, n))
