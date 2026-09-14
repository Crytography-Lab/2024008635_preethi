def encrypt(text, key):
    rails = [""] * key
    row = 0
    direction = 1

    for ch in text:
        rails[row] += ch

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    return "".join(rails)


def decrypt(cipher, key):
    if key == 1:
        return cipher

    pattern = []
    row = 0
    direction = 1

    for i in range(len(cipher)):
        pattern.append(row)

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row += direction

    rails = [""] * key

    for r in range(key):
        for i in range(len(cipher)):
            if pattern[i] == r:
                rails[r] += cipher[len("".join(rails))]

    result = ""
    index = [0] * key

    for r in pattern:
        result += rails[r][index[r]]
        index[r] += 1

    return result


text = input("Enter message: ")
key = int(input("Enter number of rails: "))

if key < 2:
    print("Number of rails must be at least 2.")
else:
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
