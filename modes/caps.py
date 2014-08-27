import string
import caps_base


def crypt(cover, plainText, color):
    '''
    Convert plaintext to ciphertext using provided cover text
    :param cover: cover text within which to hide the plaintext
    :param plainText: given plaintext to hide
    :param color: true to highlight ciphertext for debugging/visualization
    :return: ciphertext output
    '''
    return caps_base.crypt(cover, plainText, color, False)


def decrypt(cipherText):
    '''
    Decode cipherText, returning original plaintext
    '''
    return caps_base.decrypt(cipherText, False)
