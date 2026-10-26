n = int(input("Enter a number: "))
if n <= 1:
    print("Not Prime")
else:
    i = 2
    while i * i <= n:
        if n % i == 0:
            print("Not Prime")
            break
        i += 1
    else:
        print("Prime")
