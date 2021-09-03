from threading import Thread
import SC
import AO
import ALAddN


for i in range(2):
    th = Thread(target=ALAddN.connect_function, args=(i,))
    th.start()
    #th2 = Thread(target=SC.connect_function, args=(i,))
    #th2.start()
    #th3 = Thread(target=AO.connect_function, args=(i,))
    #th3.start()