import time
import multiprocessing
# with shared memory we can share data between process

def calc_square(numbers, result, v):
    v.value = 5.67
    for idx, n in enumerate(numbers):
        result[idx] = n*n

if __name__ == "__main__":
    arr = [2,3,8,9]
    #d means double, i means integer
    result = multiprocessing.Array('i',4)
    v = multiprocessing.Value('d', 0.0)
    p1 = multiprocessing.Process(target=calc_square, args=(arr,result, v))

    p1.start()
    p1.join()
    # this is way to print all the elements in array
    print(result[:])
    print(v.value)
    print("Done!")