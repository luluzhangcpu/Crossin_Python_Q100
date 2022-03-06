from functools import reduce
c = reduce(lambda x,y:x+y,[i for i in range(1,101)])
print(c)
