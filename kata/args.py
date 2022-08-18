def summa(*args):  # args - імя кортеджа в який ми передамо
    print(sum(args))            # безкінечна невизначеної довжини кількість аргументів(елементів)
summa(7,8,9,4,5,2,5,4)

def brand(**brands):  # ** з іменованими аргументами, пара ключ /значення
    print(brands)
brand(a='Apple', s='Sumsung')

def brand(**brands):
    for x,y in brands.items():  # items поверне у вигляді малих кортеджів
        print(x, ':', y)
brand(a='Apple', s='Sumsung')