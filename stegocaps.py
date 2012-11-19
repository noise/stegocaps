#!/usr/bin/python

import string

# ------------- Algorithms --------------------------------
# 'Classic' STegOcaPs: capitalize each letter in cover text that matches the plaintext
CAPS = 0
# Same as Classic but colorize for easy viewing/debugging
CAPS_COLOR = 1
# Transpose each letter in cover text that matches the plaintext with the next letter in the cover text
TRANSPOSE = 2
# Inverse of 'Classic'
CAPS_INVERSE = 4
# ---------------------------------------------------------


# For ansi color output
ENDC = '\033[0m'
BOLD = '\033[1m'


def crypt(cover, plainText, algorithm):
    '''
    Convert plaintext to ciphertext using provided cover text and algorithm
    :param cover: cover text within which to hide the plaintext
    :param plainText: given plaintext to hide
    :param alorithm: cipher method, see above for full descriptions
    :return: ciphertext output
    '''
    cover_l = list(cover.lower())
    
    cipherCap = list(cover.lower())
    cipherCapI = list(cover.upper())
    
    cipherTP = list(cover)
    
    plainText = plainText.lower()
    
    # strip out punctuation and spaces
    table = string.maketrans("","")
    plainText = plainText.translate(table, string.punctuation)
    plainText = plainText.translate(table, ' ')
    
    #    print "%s\n" % plainText
    
    j = 0
    cipherColor=""    

    for i in xrange(len(plainText)):
        while plainText[i] != cover_l[j]:
            cipherColor = cipherColor + cover[j];
            cipherCap[j] = cover_l[j]
            j = j+1
            
        cipherCap[j] = cover_l[j].upper()
        cipherCapI[j] = cipherCapI[j].lower()

        # todo: currently we can transpose the last letter of a word and the following space which breaks the words up
        # incorrectly.
        # todo: also, there's a bug if there are 2 hidden letters in a row in the cover text, need to advance +2, but then
        # we need to decouple from the other modes
        cipherTP[j-1] = cover[j]
        cipherTP[j] = cover[j-1]
        
        cipherColor = cipherColor + BOLD + cover_l[j].upper() + ENDC;

        j = j+1

    if algorithm == CAPS_COLOR:
        return "".join(cipherColor)
    elif algorithm == CAPS_INVERSE:
        return "".join(cipherCapI)
    elif algorithm == TRANSPOSE:
        return "".join(cipherTP)
    else:
        return "".join(cipherCap)


if __name__ == '__main__':

    # TODO: command-line args
    # --cover (file)
    # --secret (file or string)
    # --color
    # --mode/algo
    plainText = "This is some hidden text, see?"

    cover = "The primary function of chemical nomenclature is to ensure that a spoken or written chemical name leaves no ambiguity concerning to what chemical compound the name refers: each chemical name should refer to a single substance. A less important aim is to ensure that each substance has a single name, although the number of acceptable names is limited.\
Preferably, the name also conveys some information about the structure or chemistry of a compound. CAS numbers form an extreme example of names that do not perform this function: each CAS number refers to a single compound but none contain information about the structure.\
The form of nomenclature used depends on the audience to which it is addressed. As such, no single correct form exists, but rather there are different forms that are more or less appropriate in different circumstances.\
A common name will often suffice to identify a chemical compound in a particular set of circumstances. To be more generally applicable, the name should indicate at least the chemical formula. To be more specific still, the three-dimensional arrangement of the atoms may need to be specified. \
In a few specific circumstances (such as the construction of large indices), it becomes necessary to ensure that each compound has a unique name: This requires the addition of extra rules to the standard IUPAC system (the CAS system is the most commonly used in this context), at the expense of having names that are longer and less familiar to most readers. Another system gaining popularity is the International Chemical Identifier (InChI) while InChI symbols are not human-readable, they contain complete information about substance structure. That makes them more general than CAS numbers.\
The IUPAC system is often criticized for the above failures when they become relevant (for example, in differing reactivity of sulfur allotropes, which IUPAC does not distinguish). While IUPAC has a human-readable advantage over CAS numbering, it would be difficult to claim that the IUPAC names for some larger, relevant molecules (such as rapamycin) are human-readable, and so most researchers simply use the informal names.\
"

    cipher = crypt(cover, plainText, CAPS)
    print cipher
    print
    
    cipher = crypt(cover, plainText, CAPS_COLOR)
    print cipher
    print

    cipher = crypt(cover, plainText, TRANSPOSE)
    print cipher
    print

    cipher = crypt(cover, plainText, CAPS_INVERSE)
    print cipher
    print
