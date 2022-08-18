tuple = ('first',25,25.1,)
# кортедж не змінюється
print (tuple)

# кортедж в список list, в кортедж - tuple

# print(list((45,45,148,64))
# КЛЮЧ:ЗНАЧЕННЯ
dict = {'apple':'green','orange':'orange','banan':'yellow'}
print(dict)

for k in dict.keys():
    print(k)

for k in dict.values():
    print(k)

for k in dict.items():
    print(k)
# ДРУКУЄМ ЗНАЧЕННЯ
print(dict['banan'])
# ЗМІНЮЄМО ЗНАЧЕННЯ
dict['banan'] = 'green'
print(dict)
# ВИДАЛЯЄМО
del(dict['banan'])
print(dict)