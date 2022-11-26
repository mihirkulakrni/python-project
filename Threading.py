import threading
import time

def myfunction():
    print("Start Thread")
    time.sleep(3)
    print("End Thread")

threads = []

for i in range (5) :
     myfunction()
