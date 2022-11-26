print("IF NESTING")
x = "Cisco"

if "i" in x:
    if len(x) > 3:
        print(x, len(x))

        
print("for nesting")
list1 = [4, 5, 6]
list2 = [10, 20, 30]
for i in list1:

    for j in list2: 
        print(i*j)
print("while nesting")
x = 1
while x <= 10:
    
    z = 5
    x += 1
    while z <= 10:
        print(z)
        z+=1
        
print("mixed nesting")	
for number in range(10):
    if 5 <= number <= 9:
        print(number)
           
	
	 
