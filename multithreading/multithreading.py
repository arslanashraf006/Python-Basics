import time
import threading

def calc_square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('square:',n*n)


def calc_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

array = [2,3,8,9]

t = time.time()
t1 = threading.Thread(target=calc_square, args=(array,))
t2 = threading.Thread(target=calc_cube, args=(array,))

t1.start()
t2.start()

#join Wait until the thread terminates.
t1.join()
t2.join()
print("done in: ", time.time()-t)
print("Hah... I am done with all my work now!")