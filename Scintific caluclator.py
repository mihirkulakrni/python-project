import math

while True :
    
    print("\n choose the opreation. \n\n0 - Addition\n1 - Substraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - raising a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n8 - Cosine\n10 - Tanget\n")
    
    oper = input("Enter Your Option")

#Addition

    if oper == '0':
        val1 = float(input("\n Enter The First Value: "))
        val2 = float(input("\n Enter The Second Value: "))

        print("\n The result is: " + str(val1+val2)+"\n")

        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break
#Substraction

    elif oper == '1':
        val1 = float(input("\n Enter The First Value: "))
        val2 = float(input("\n Enter The Second Value: "))

        print("\n The result is: " + str(val1-val2)+"\n")

        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break

# Multiplication
    elif oper == '2':
        val1 = float(input("Enter The First Value: "))
        val2 = float(input("Enter The Second Value: "))
        print("\n The result is:" + str(val1 * val2)+ "\n")
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
         
            continue
        else:
            break
# Division

    elif oper == '3':
        val1 = float(input("Enter The First Value: "))
        val2 = float(input("Enter The Second Value: "))
        print("\n The result is:" + str(val1 / val2)+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break
#Modulo
    elif oper == '4':
        val1 = float(input("Enter The First Value: "))
        val2 = float(input("Enter The Second Value: "))
        print("\n The result is:" + str(val1 % val2)+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break            
#Raising A Power
    elif oper == '5':
        val1 = float(input("Enter The First Value:"))
        val2 = float(input("Enter The Second Value: "))
        print("\n The result is:" + str(math.pow(val1 , val2))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break
#Square root            
    elif oper == '6':
        val1 = float(input("Enter The First Value: "))
        
        print("\n The result is:" + str(math.sqrt(val1))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break
#Logarithm
    elif oper == '7':
        val1 = float(input("Enter The Value for calulating the lograthim to base of 2: "))
        
        print("\n The result is:" + str(math.log(val1,2 ))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break        
#Sing
    elif oper == '8':
        val1 = float(input("Enter The First Value(in degress to calulating the sine: )"))
        
        print("\n The result is:" + str(math.sin(math.radians(val1)))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break
#Cosin
    elif oper == '9':
        val1 = float(input("Enter The First Value(in degress to calulating Cosin: )"))
        
        print("\n The result is:" + str(math.cos(math.radians(val1 )))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break   
#Tangent

    elif oper == '10':
        val1 = float(input("Enter The First Value(in degrees for calulating the tangent)"))
        
        print("\n The result is:" + str(math.tan(math.radians(val1 )))+ "\n")       
        back = input("\n Do you want to go back to menu? (Prees y/n)")

        if back == 'y':
            continue
        else:
            break

#invalid option
    else:
        print("\n Invlid Option \n")
        continue


#End Of Program    
#Scintific laulator by Mihir 