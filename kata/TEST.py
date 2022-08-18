d = lambda p: p * 2
t = lambda p: p * 3
x = 2
x = d(x)
x = t(x)
x = d(x)
print(x)


name = "snow storm"
print("%s" % name[6:8])

a = [1,2,3,None,(),[],]
print(len(a))



a = b = c = [1, 2, 3]
b.append(4)
c.pop(2)
a.extend(c)
print(a)