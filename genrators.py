#Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
my_list = ["1","2","3","4","5","6","7","8"]
my_list
['1', '2', '3', '4', '5', '6', '7', '8']
for element in my_list:
    print(element)

    

my_iter = iter(my_list)
type my_iter

type (my_iter)

next(my_iter)
'1'
next(my_iter)
'2'


next(my_iter)
'3'
next(my_iter)
'4'
next(my_iter)
'5'
next(my_iter)
'6'
next(my_iter)
'7'
next(my_iter)
'8'
#no more furteher because list is end u will get syntac eroor lets me show u
next(my_iter)





#genrators
def my_gen(x ,y):
    for i in range(x):
        print("i is %d",% i)
        
SyntaxError: invalid syntax
def my_gen(x ,y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield 1 * y

        
my_object = my_gen(10,5)
my_object
<generator object my_gen at 0x0000029D959E2570>
type(my_object)
<class 'generator'>
next(my_object)
i is 0
y is 5
5
