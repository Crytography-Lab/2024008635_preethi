def encrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')

            if ch.isupper():
                result += chr(
                    (ord(ch) - ord('A') + shift) % 26 + ord('A')
                )
            else:
                result += chr(
                    (ord(ch) - ord('a') + shift) % 26 + ord('a')
                )

            j += 1
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""
    key = key.upper()
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % len(key)]) - ord('A')

            if ch.isupper():
                result += chr(
                    (ord(ch) - ord('A') - shift) % 26 + ord('A')
                )
            else:
                result += chr(
                    (ord(ch) - ord('a') - shift) % 26 + ord('a')
                )

            j += 1
        else:
            result += ch

    return result


text = input("Enter message: ")
key = input("Enter key: ")

encrypted = encrypt(text, key)
decrypted = decrypt(encrypted, key)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)
