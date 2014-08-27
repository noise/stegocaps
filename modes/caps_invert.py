import caps_base


def crypt(cover, plainText, color):
    '''
    Convert plaintext to ciphertext using provided cover text
    :param cover: cover text within which to hide the plaintext
    :param plainText: given plaintext to hide
    :return: ciphertext output
    '''
    return caps_base.crypt(cover, plainText, color, True)

def decrypt(cipherText):
    '''
    Decode cipherText, returning original plaintext
    '''
    return caps_base.decrypt(cipherText, True)
