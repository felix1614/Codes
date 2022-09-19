import threading
import time
from threading import Thread


def smile(*stringvav):
    print(stringvav[0], threading.currentThread().getName())
    time.sleep(stringvav[1])
    thre()
    smile(*stringvav)


def thre():
    print("inside thre", threading.currentThread().getName())
    c1 = Thread(target=smile, args=["hello", 20, ], name="c1")
    c2 = Thread(target=smile, args=["bye", 10, ], name="c2")
    c3 = Thread(target=smile, args=["hiii", 30, ], name="c3")

    c1.start()
    c2.start()
    c3.start()
    print("finished")

thre()