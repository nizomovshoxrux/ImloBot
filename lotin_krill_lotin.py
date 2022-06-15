from transliterate import to_cyrillic, to_latin

def wordTranslator(word):
    
    javob = lambda word: to_cyrillic(word) if word.isascii() else to_latin(word)
    
    return javob(word)





