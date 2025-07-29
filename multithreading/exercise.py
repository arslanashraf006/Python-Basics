import time
import threading
def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake." % i)


for i in range(10):
    th = threading.Thread(target=sleepMe, args=(i,))
    th.start()
    print("Current Threads: %i." % threading.active_count())