from threading import Thread
from random import randint
import time

def sleep_print():
    r = randint(0,3)
    time.sleep(r)
    print(f"Hello : {r}")


t1 = Thread(target=sleep_print)
t2 = Thread(target=sleep_print)

t1.start()
t2.start()

t1.join()
t2.join()
