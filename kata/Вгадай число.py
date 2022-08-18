import random
number = random.randint(1,10)
for i in range(3):
     a = int(input('Введи число від 1 до 10:\n'))
     if a < number:
          print('Фігушки, число більше')
     elif a > number:
          print('Фігушки, число менше')
     elif a == number:
          print('Уррааа!!!!')