
def product10(a):
    return a *10

r1 = range(10)
map(product10,r1)
#<map object at 0x0000022807FB1150>
list(map(product10,r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


map((lambda a: a *10),r1)
#<map object at 0x0000022807FB0370>
list(map((lambda a: a *10),r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
filter(map((lambda a: a>5),r1))

filter((lambda a: a>5),r1)
#filter object at 0x0000022807FB11E0
list(filter((lambda a: a>5),r1))
[6, 7, 8, 9]
