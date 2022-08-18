def disemvowel(string_):
    vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
    return ''.join([l for l in string_ if l not in vowels])