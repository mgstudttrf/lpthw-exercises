def breakwords(stuff):
    return stuff.split(' ')

def sortwords(words):
    return sorted(words)

def printfirst(words):
    """blah blah"""
    print(words.pop(0))

def printlast(words):
    print(words.pop(-1))

def sortsentence(sentence):
    return sortwords(breakwords(sentence))

def printfirstlast(sentence):
    breakz = breakwords(sentence)
    printfirst(breakz)
    printlast(breakz)

def printflsorted(sentence):
    sortz = sortwords(breakwords(sentence))
    printfirst(sortz)
    printlast(sortz)
