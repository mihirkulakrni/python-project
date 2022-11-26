#TO CONVERT M/S TO K/HR AND KM/HR TO M/S

print ("ENTER WHICH YOU WANT TO CONVERT M/S OR KM/HR")
choice = input("Enter your choice: ")
if choice == "KM/HR" :
    x = int (input("Enter Value")) #
    v  = x*18/5
    print(v)   
elif choice == "M/S":
     x = int (input("Enter Value"))
     v  = x*5/18
     print(v)  
    
    
