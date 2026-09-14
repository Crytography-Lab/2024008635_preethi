def get_order(key):
    return sorted(range(len(key)), key=lambda i: (key[i], i))


def columnar_encrypt(text, key):
    text = text.replace(" ", "")
    columns = len(key)
    rows = (len(text) + columns - 1) // columns

    text += 'X' * (rows * columns - len(text))

    matrix = []

    for i in range(0, len(text), columns):
        matrix.append(text[i:i + columns])

    order = get_order(key)

    result = ""

    for col in order:
        for row in range(rows):
            result += matrix[row][col]

    return result


def columnar_decrypt(cipher, key):
    columns = len(key)
    rows = len(cipher) // columns

    order = get_order(key)
    matrix = [[''] * columns for _ in range(rows)]

    index = 0

    for col in order:
        for row in range(rows):
            matrix[row][col] = cipher[index]
            index += 1

    result = ""

    for row in range(rows):
        for col in range(columns):
            result += matrix[row][col]

    return result


def encrypt(text, key1, key2):
    first = columnar_encrypt(text, key1)
    second = columnar_encrypt(first, key2)

    return second


def decrypt(cipher, key1, key2):
    second = columnar_decrypt(cipher, key2)
    first = columnar_decrypt(second, key1)

    return first


text = input("Enter message: ")
key1 = input("Enter first key: ")
key2 = input("Enter second key: ")

encrypted = encrypt(text, key1, key2)
decrypted = decrypt(encrypted, key1, key2)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
