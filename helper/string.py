import unicodedata

def rmDigits(string):
    result = ''.join([i for i in string if not i.isdigit()])
    return result

def strNormalize(string):
    return unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII').replace('  ','').replace('\n','').replace('\r','').strip()
