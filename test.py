import threading
import time
import random
def test1(cmt:int)->None:
    print(cmt,i)
    time.sleep(random.random())
def test2(cmt:int)->None:
    for i in range(10):
        print(cmt,i)
        time.sleep(random.random())
b=True
i=0
while b:
    if i<=9:
        ms=[th.name for th in threading.enumerate()]
        if ms.count("test1")<=2:
            threading.Thread(target=test1,args=(i,),name="test").start()
        if ms.count("test2")<=3:
            threading.Thread(target=test1,args=(i,),name="test{}".format(i))
    else:
        break
    i+=1