a = int(input("Enter dividend : "))
b = int(input("Enter divisor: "))
if b == 0:
    print("Division by zero is not allowed")
else:
    q = a // b
    r = a % b
    print("Quotient = ", q)
    print("Remainder = ", r)
    print(f"{a} = {b} x {q} + {r}")
