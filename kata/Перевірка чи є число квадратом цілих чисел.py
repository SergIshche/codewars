def is_square(n):
    return n >= 0 and (n**0.5) % 1 == 0

print(is_square(81))



import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;