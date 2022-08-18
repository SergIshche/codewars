pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])

скільки разів мячик пролетить повз вікно

def bouncing_ball(h, bounce, window):
    if h < 0 or bounce >= 1 or bounce < 0 or window >= h:
        return -1
    else:
        count = 1
        h1 = h*bounce
        while h1 > window:
            h1*=bounce
            count += 2
        return count