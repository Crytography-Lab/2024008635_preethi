def create_matrix(key):
    key = key.upper().replace("J", "I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    letters = ""

    for ch in key + alphabet:
        if ch.isalpha() and ch not in letters:
            letters += ch

    matrix = []

    for i in range(0, 25, 5):
        matrix.append(letters[i:i + 5])

    return matrix


def find_position(matrix, ch):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == ch:
                return row, col

    return None


def prepare_text(text):
    text = text.upper().replace("J", "I")
    text = "".join(ch for ch in text if ch.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 == len(text):
            result += a + "X"
            i += 1

        elif text[i + 1] == a:
            result += a + "X"
            i += 1

        else:
            result += a + text[i + 1]
            i += 2

    return result


def encrypt(text, key):
    matrix = create_matrix(key)
    text = prepare_text(text)

    result = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]

        elif col1 == col2:
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]

        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


def decrypt(text, key):
    matrix = create_matrix(key)
    result = ""

    for i in range(0, len(text), 2):
        a = text[i]
        b = text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result += matrix[row1][(col1 - 1) % 5]
            result += matrix[row2][(col2 - 1) % 5]

        elif col1 == col2:
            result += matrix[(row1 - 1) % 5][col1]
            result += matrix[(row2 - 1) % 5][col2]

        else:
            result += matrix[row1][col2]
            result += matrix[row2][col1]

    return result


key = input("Enter key: ")
text = input("Enter message: ")

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)
