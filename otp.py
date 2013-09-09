from os import urandom


def otp_encode(plaintext):
    key = bytearray(urandom(len(plaintext)))
    ciphertext = bytearray()
    for a, b in zip(bytearray(plaintext), bytearray(key)):
        ciphertext.append(a ^ b)
    return ciphertext, key


def otp_decode(ciphertext, key):
    plaintext = bytearray()
    for a, b in zip(bytearray(ciphertext), bytearray(key)):
        plaintext.append(a ^ b)
    return plaintext
