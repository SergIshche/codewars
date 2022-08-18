def alphabet_position(text):
    a = "abcdefghijklmnopqrstuvwxyz"
    return " ".join([str(a.find(c) + 1) for c in text.lower() if c in a])
    pass

print(alphabet_position('bddxb dxfb dbbddxd xbxb x bzz'))