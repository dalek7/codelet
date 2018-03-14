#-*- coding: utf-8 -*-

z1 = (lambda x,y: x + y)(10, 20)
print(z1)

#z1 = (lambda x: x ** 2)(range(5)) # not working
#print(z1)

# map(함수, sequence, sequence, ...)
z1 = map((lambda x: x ** 2), range(5)) # Python 2
print(z1)

z1 = list(map(lambda x: x ** 2, range(5))) # Python 2 & 3
print(z1)