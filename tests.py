from . import otp


def encode_decode_test():
    assert(otp.otp_decode(*otp.otp_encode('test string')) == 'test string')
