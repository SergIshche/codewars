import string

def is_pangram(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for x in alphabet:
        if x not in s.lower():
            return False
    return True