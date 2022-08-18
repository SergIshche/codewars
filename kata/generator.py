print(sum([i ** 3 for i in range(1,21) if i % 5 ==0]))  # сума список від 1 до 20 які дфляться на 5 в кубі

s = []
for i in range(1,21):
    for j in range(1,51):
        s.append((i,j))
print(s)

print([(i,j) for i in range(1,21) for j in range(1,51)])

s1 =[]
for i in range (-10,11):
    if i > 0:
        s1.append(i**2)
    else:
        s1.append(i**3)
print(s1)

print([i**2 if i>0 else i**3 for i in range(-10,11) if i %2 ==0])

s= [7,8,8,-10,-10]
set_set = {i for i in s}
print(set_set)
dictionary = {i: i**10 for i in s}
print(dictionary)