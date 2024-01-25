# Hands on 2 - Selection Sort

import random
import time
import tracemalloc

A = [5, 2, 4, 6, 1, 3]
B = [31, 41, 59, 26, 41, 58, 32, 97, 93, 12]
C = [random.randint(1, 2^16) for i in range(1, pow(2, 16))] # Array with 2^16 (65,536) random elements

def selection_sort(array):
    tracemalloc.start()
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()


if __name__ == '__main__':
    print("Selection Sort")
    tA = time.time()
    selection_sort(A)
    tA = time.time() - tA
    print('A: ', tA)

    tB = time.time()
    selection_sort(B)
    tB = time.time() - tB
    print('B: ', tB)

    tC = time.time()
    selection_sort(C)
    tC = time.time() - tC
    print('C: ', tC)

