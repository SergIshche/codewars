n = int(input())

b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2
return b




def add_binary(a,b):   #сума двох чисел в бінарний
    return bin(a+b)[2:]

print(add_binary(545,64622))