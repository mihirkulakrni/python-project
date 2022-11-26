
def my_gen(x ,y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield 1 * y

my_object = my_gen(10,5)
my_object

type(my_object)

next(my_object)
i is 0
y is 5
5
def my_gen(x ,y):
    for i in range(x):
        print("i is %d" % i)
        print("y is %d" % y)
        yield i * y

        
my_object = my_gen(10,5)
next(my_object)
i is 0
y is 5

next(my_object)
i is 1
y is 5

next(my_object)
i is 2
y is 5


next(my_object)
i is 3
y is 5

next(my_object)
i is 4
y is 5

next(my_object)
i is 5
y is 5

next(my_object)
i is 6
y is 5

next(my_object)
i is 7
y is 5

next(my_object)
i is 8
y is 5

next(my_object)
i is 9
y is 5

next(my_object)

# exuasteed
next(my_object)



type(gen_exp)

next(gen_exp)

next(gen_exp)

next(gen_exp)
next(gen_exp)

next(gen_exp)
