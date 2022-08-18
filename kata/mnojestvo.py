ttt = set()   #сет - множество
print(type(ttt))
spisok = set([1,1,2,2,4,5,6,8,9,4])
spisok1 = list(spisok)
print(spisok)
print(spisok1)

num = {1,2,3,4,5,6,7,8,6,4}
for i in num:
    print(i)
print(3 in num)
num.add(58)  # добавить в список
print(num)
#.remove - видалить з помилкоб якщо був відсутній в множестві
#.discard - удалить без вивода ошибки якщо відсутній
#.pop   - видаляє перший елемент
#.clear - видаляє всі елементи
#num3=num.union(num2) або num | num2 - об"єднує множества
#num3=num.intersection(num2) або num & num2 - повернтає множество з елементами які є  в обох
numbers = frozenset({1,2,5,6,4,3})
numbers2 = {5,6,4,7,89,46}
numbers3 = len(numbers2)
print(numbers)
num3 = num2.copy
#.copy - скопировать множество