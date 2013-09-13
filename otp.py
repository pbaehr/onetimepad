from os import urandom


def xor_bytearray(ba1, ba2):
    c = bytearray()
    for a, b in zip(ba1, ba2):
        c.append(a ^ b)
    return c


def otp_encode(plaintext):
    key = bytearray(urandom(len(plaintext)))
    ciphertext = xor_bytearray(bytearray(plaintext), key)
    return ciphertext, key


def otp_decode(ciphertext, key):
    plaintext = xor_bytearray(bytearray(ciphertext), bytearray(key))
    return plaintext
