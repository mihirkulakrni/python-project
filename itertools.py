Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from itertools import *
list1 = [1,2,3,4,5, "a","b"]
list2 = [15,29,5,46,15, "X","Y"]
chain(list1 , list2)
<itertools.chain object at 0x00000223F2841420>
for i in chain(list1, list2):
    print(i)

    
1
2
3
4
5
a
b
15
29
5
46
15
X
Y
list(chain(list1,list2))
[1, 2, 3, 4, 5, 'a', 'b', 15, 29, 5, 46, 15, 'X', 'Y']
for i in count(10,2.:5)
SyntaxError: expected ':'
for i in count(20, 2.5):
    if i <= 50:
        print(i)
    else:
        break

    
20
22.5
25.0
27.5
30.0
32.5
35.0
37.5
40.0
42.5
45.0
47.5
50.0
37.5
37.5






filterfalse(lambda x: x< 5 ,[],2,3,45,6,7)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    filterfalse(lambda x: x< 5 ,[],2,3,45,6,7)
TypeError: filterfalse expected 2 arguments, got 7

filterfalse(lambda x: x < 5 ,[1,2,3,4,5,6,7])
<itertools.filterfalse object at 0x00000223F2843F10>
list(filterfalse(lambda x:; x< 5 , [1,2,3,4,5,6,7]))
SyntaxError: invalid syntax
list(filterfalse(lambda x: x< 5 , [1,2,3,4,5,6,7]))
[5, 6, 7]
range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(10))[2:9:2]
[2, 4, 6, 8]
islice(range(10),2,9,2)
<itertools.islice object at 0x00000223F283F060>
list(islice(range(10),2,9,2))
[2, 4, 6, 8]
