names = ['kesha','gus', 'kitsa']

for name in names:
    print(name)
print (names[-2])
names.pop()
names.append('los')
print(names)

n= names.index('los')
print(n)

numbers = [4,65,54,54,22,6,4,8]
numbers.sort(reverse=True)
numbers[2] = 'b'
print(numbers)