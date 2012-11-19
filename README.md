# Overview

STegOcaPs is a collection of simple text-based steganography (http://en.wikipedia.org/wiki/Steganography) implementations based around hiding the secret text in a cover text by manipulating the capitalization of the cover text letters.

I originally had the idea for the classic StegoCaps in 2005 but never got around to implementing it. I certainly never assumed that I was the first to consider this technique but hadn't looked around for other mentions or implementations of it. Now that I've implemented a basic version I decided to do some research, findings are below.

It's somewhat questionable if the more basic algorithms herein are truly steganography as they are not terribly effetive at hiding the existence of the secret, but it's still fun!

# Algorithms

* (/) Caps
* (/) Inverse caps
* (/) Transposition - transpose each target letter with the letter following it.
* bit-based stegocaps
* bit-based word-spacing stego - see https://www.waset.org/journals/ijcie/v4/v4-2-15.pdf
* use of accents and odd punctuation? or unicode chars that look like normal english chars?


# Todo

* generate lorem ipsum text for cover
* fetch random wikipedia text for cover
* repeat text to needed length for cover
* truncate text to needed length for cover
* protection against overflow/exhaustion of cover
* unit tests

# Related tools and research

* 1996: Mimic Functions by Peter Wayner (1996) - http://www.wayner.org/node/13
** http://www.nic.funet.fi/pub/crypt/old/mimic/mimic.text
** http://www.spammimic.com
* 2005: Kavascript stego encoding source text as 2-byte indexes into a dictionary of words, producing gibberish : http://www.fourmilab.ch/javascrypt/stego.html
* 2005: Hide secret text in language translation errors, fancy! https://www.cerias.purdue.edu/assets/pdf/bibtex_archive/2005-39.pdf
* 2010?: Nit-based word-spacing stego: https://www.waset.org/journals/ijcie/v4/v4-2-15.pdf
* ???? : Snow uses trailing whitespace (clever!): http://www.darkside.com.au/snow/index.html

Also see this big list of all varieties of stego tools: http://www.jjtc.com/Steganography/tools.html (lots of dead links unfortunately)

