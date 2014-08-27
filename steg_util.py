import string

# For ansi color output
ENDC = '\033[0m'
BOLD = '\033[1m'

def isUsableLetter(letter):
    return letter not in string.punctuation and letter != ' '

def cleanPlaintext(plainText):
    # strip out punctuation and spaces
    table = string.maketrans("", "")
    plainText = plainText.translate(table, string.punctuation)
    plainText = plainText.translate(table, ' ')
    plainText = plainText.translate(table, '\n')
    # todo screen all non-alphanumerics
    return plainText
