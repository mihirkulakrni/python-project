import threading
import time

def myfunction():
    print("Start   thread")
    time.sleep(3)
    print("End   thread")

    
threads = []

for i in range(10):
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)


for th in threads:
    th.join()    
