#calculate speed/distance/time in km/hr
   
ch = input ("ENTER YOUR CHOICE SPEED/DISTANCE/TIME/ IN KM/HR")

if ch== 'SPEED':
    d = int(input("ENTER YOUR DISTANCE IN KM ="))
    t = int(input("ENTER YOUR TIME IN HOUR ="))
    s = d/t
    print ("SPEED WILL BE",s,"KM/HR")
elif ch== 'TIME':
    d = int(input("ENTER YOUR DISTANCE IN KM ="))
    s = int(input("ENTER YOUR SPEED KM\HOUR ="))
    t = s*d
    print ("TIME WILL BE",t,"HOUR")
    
elif ch== 'DISTANCE':
    s = int(input("ENTER YOUR SPEED IN KM/HR ="))
    t = int(input("ENTER YOUR TIME IN HOUR ="))
    d = s*t
    print ("DISTANCE WILL BE",d,"KM")    
