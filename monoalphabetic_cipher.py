def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                result += key[ord(ch) - ord('A')].upper()
            else:
                result += key[ord(ch) - ord('a')].lower()
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isalpha():
            if ch.isupper():
                index = key.upper().index(ch)
                result += chr(index + ord('A'))
            else:
                index = key.lower().index(ch)
                result += chr(index + ord('a'))
        else:
            result += ch

    return result


text = input("Enter message: ")
key = input("Enter 26-letter key: ")

if len(key) != 26 or not key.isalpha() or len(set(key.upper())) != 26:
    print("Invalid key! Enter 26 unique letters.")
else:
    encrypted = encrypt(text, key)
    decrypted = decrypt(encrypted, key)

    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypted)
