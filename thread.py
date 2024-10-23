from threading import Thread
from time import *
def task1():
    for i in range(10):
        sleep(0.5)
        print('task #1: %d'%(i))
    print('task #1 selesai')

def task2():
    for i in range(10):
        sleep(0.5)
        print('task #2: %d'%(i))
    print('task #2 selesai')

if __name__ == "__main__":
    print('Main program')
    t1 = Thread(target=task1, name='t1')
    t2 = Thread(target=task2, name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    for i in range(10):
        print('Main Program: %d'%(i))
    print('Main Program selesai')
