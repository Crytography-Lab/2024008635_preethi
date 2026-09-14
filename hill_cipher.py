key = [[3, 3], [2, 5]]
inv_key = [[15, 17], [20, 9]]


def encrypt(text):
    text = text.upper().replace(" ", "")

    if len(text) % 2 != 0:
        text += 'X'

    result = ""

    for i in range(0, len(text), 2):
        a = ord(text[i]) - 65
        b = ord(text[i + 1]) - 65

        x = key[0][0] * a + key[0][1] * b
        y = key[1][0] * a + key[1][1] * b

        result += chr(x % 26 + 65)
        result += chr(y % 26 + 65)

    return result


def decrypt(text):
    result = ""

    for i in range(0, len(text), 2):
        a = ord(text[i]) - 65
        b = ord(text[i + 1]) - 65

        x = inv_key[0][0] * a + inv_key[0][1] * b
        y = inv_key[1][0] * a + inv_key[1][1] * b

        result += chr(x % 26 + 65)
        result += chr(y % 26 + 65)

    return result


message = input("Enter message: ")

encrypted = encrypt(message)
decrypted = decrypt(encrypted)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
