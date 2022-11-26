Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def product10(a):
    return a *10

r1 = range(10)
map(product10,r1)
<map object at 0x0000022807FB1150>
list(map(product10,r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


map((lambda a: a *10),r1)
<map object at 0x0000022807FB0370>
list(map((lambda a: a *10),r1))
[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
filter(map((lambda a: a>5),r1))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    filter(map((lambda a: a>5),r1))
TypeError: filter expected 2 arguments, got 1
filter((lambda a: a>5),r1)
<filter object at 0x0000022807FB11E0>
list(filter((lambda a: a>5),r1))
[6, 7, 8, 9]
