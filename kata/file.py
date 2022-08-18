
# створили файл 1 txt, записали в нього, закрили. w - запис, r - читати
f = open('1.txt', 'w')
f.write('hi, file')
f.close
# a - режим додавання
with open('1.txt','a') as f:
    f.write(' da da da')


try:
    a = int(input('a: '))
    b = int(input('b: '))
    print((a / b))
except ZeroDivisionError: # якщо ввели 0 - помилка
    print("na 0 ne deli")
