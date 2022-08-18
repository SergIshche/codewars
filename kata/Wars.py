def generate_hashtag(s):

    if len(s)>140:
        return False
    elif s == "":
        return False
    else:
        s.capitalize()
        return "#" + s.replace(' ', '')

generate_hashtag("jtj cfjcmcmm")