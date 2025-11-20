alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def decryptvigenere(ciphertext, key):
    plaintext = ""
    ciphertext = ciphertext.replace(" ", "")
    key = key.upper()

    for index in range(len(ciphertext)):
        ciphertextindex = alphabet.index(ciphertext[index])
        keyindex = alphabet.index(key[index % len(key)])
        plaintextindex = (ciphertextindex - keyindex) % 26

        plaintext += alphabet[plaintextindex]

    return plaintext

