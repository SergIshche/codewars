import re

str = 'ac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dcac/dc'
result = re.match('ac', str) # на початку строки
print(result)

result = re.search('dc', str) # перше яке знайде в строкі
print(result)

result = re.findall('dc', str) # виводе список всіх в строкі
print(result)

result = re.split('/', str) # розбиває по заданому символу строку і виводе список
print(result)

result = re.split('/', str, maxsplit=3) # розбиває N раз, далі строка яка залишилася
print(result)

result = re.sub('a', 'b', str) # заміна одного елемента на інший
print(result)

result = re.fullmatch('a', str) # перевіряє повний збіг
print(result)

# ------------------------------------------------------------------------

s = '65651651+51165165      --- - - 56554gjgvmvh, ,GDGFhgnNgN gnNG.!!!'
result = re.search(r'g.g',s) # r'[]' - сира строка, вікдключе наприклад / як перенос тексту
print(result)  # . - заміняє любий символ
                # \d - перша цифра | \d\d\d - три цифри підряд | \D - перше значення відмінне від цифри
result = re.search(r'\s',s) # виведе пробіл \S - навпаки - виведе перший не пробіл
print(result)

result = re.search(r'\w',s) # люба буква, цифра, нижнє підкреслення | \W - навпаки
print(result)

result = re.search(r'\b',s) # початок нового слова \B - якщо в середині слова
print(result)

result = re.search(r'\d*',s) # 0 чи  більше входжень | + 1 і більше входжень
print(result)

result = re.search(r'[iugl]',s) # знаходить перший збіг з заданої строки
print(result)

result = re.search(r'[1-5]',s) # знаходить перший збіг з заданої строки, діапазон
print(result)

result = re.search(r'[^4-6]',s) # знаходить перший який не входить
print(result)

result = re.search(r'H|f',s) # виведе те що перишим знайде (H або f)
print(result)

result = re.search(r'\d{3}',s) # квантіфікатор. виведе = \d\d\d
print(result)

result = re.search(r'\d{4,}',s) # квантіфікатор. виведе не менше ніж 4 підряд йдущих цифри
print(result)

result = re.search(r'\d{,4}',s) # квантіфікатор. виведе не більщ ніж 4 підряд йдущих цифри
print(result)

str1 = "Привет! Как дела? А у меня нормально."
result = re.findall(r'[бвгджзклмнпрстфхчшщБВГДЖЗКЛМНПРСТФХЧШЩ]\w+', str1)
print(result)