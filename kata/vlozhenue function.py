import builtins
print(dir(builtins)) # встроєні функції пайтон

y=2
def degree(x):
    y = 3     # локальна перемінна - існує тільки в цій функції
    def degree_two():
        return y**x
    return degree_two()
print(degree(4))
print(y)

def message(number):
    def print_message():
        return 'Chislo - ' + str(number)
    return print_message()
print(message(78))


def message(x):
    def print_message(y):
        return x,y
    return print_message
d = message(4)  # жива ссилка, запам"ятали це значення в функції
print(d)
print(d(8))
print(d(4))
print(d(3))
print(d(98))