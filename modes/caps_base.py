import steg_util


def crypt(cover, plainText, color, invert):
    '''
    Convert plaintext to ciphertext using provided cover text
    :param cover: cover text within which to hide the plaintext
    :param plainText: given plaintext to hide
    :param color: true to output ansi color sequences to highlight hidden text
    :param invert: true to start with uppercase and encode w/lower
    :return: ciphertext output
    '''
    #print "color: %s, invert: %s" % (color, invert)
    #print plainText
    
    if invert:
        coverColor = list(cover.upper())
        cipherCap = list(cover.upper())
    else:
        coverColor = list(cover.lower())
        cipherCap = list(cover.lower())

    plainText = steg_util.cleanPlaintext(plainText)
    plainText = plainText.lower()
    cover_l = cover.lower()

    j = 0
    cipherColor = ""

    for i in xrange(len(plainText)):
        while plainText[i] != cover_l[j]:
            if color:
                cipherColor = cipherColor + coverColor[j]

            #cipherCap[j] = cover_l[j]
            j = j + 1

        if invert:
            cipherCap[j] = cipherCap[j].lower()
        else:
            cipherCap[j] = cipherCap[j].upper()

        if color and invert:
            cipherColor = cipherColor + steg_util.BOLD + coverColor[j].lower() + steg_util.ENDC;
        elif color:
            cipherColor = cipherColor + steg_util.BOLD + coverColor[j].upper() + steg_util.ENDC;

        j = j + 1

        
    if color:        
        return "".join(cipherColor) + "".join(coverColor[j:])
    else:
        return "".join(cipherCap)


def decrypt(cipherText, invert):
    secret = ""
    for i in xrange(len(cipherText)):
        if (invert and cipherText[i].islower()) or ( not invert and  cipherText[i].isupper()):
                secret = secret + cipherText[i]
    return secret
