#import os
#print(os.getcwd())    перевірка місця куди зберігає
# https://www.youtube.com/watch?v=UDthAJmD3EQ&list=PLs2IpQwiXpT3SqbqPzLCEy1fow9G7g0oY&index=15

with open('map.txt') as f:
    n = int(f.readline())
    for i in range(n):
        a, b = map(int, f.readline().split())
        print(a + b)

def f(a,b):
    return a*b

a = map(f, [2,4,5],[5,6,7])  # перемножили елементи першого списка на елементи другого
print(list(a))

a = map(lambda x: x+15, (2,4,5))
print(list(a))

def f(a):
    if a%2 == 0:
        return a
a = filter(f,(2,4,5,5,9,8,6,1,5,4))    # відфільтрували парні числа
print(list(a))

a = filter(lambda x:(x%2==0),(2,4,5,68,64,5))  # відфільтрували парні числа
print(list(a))

from functools import reduce
print(reduce(lambda a,b:a*b,(50,54,89,12,100)))  # перемножили всі елементи між собою

a = [1,2,3,4,5,6]
b = 'abcdef'
result = zip(a,b)     # згропували елементи між собою в кортеджі і все це вивели в список
print(list(result))






    #first = list(map(int, r))
    #second = filter(lambda first: (first % 5 == 0), first)
    #print(list(second))