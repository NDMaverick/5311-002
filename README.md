# CSE 5311-002 - Hands On 2

Implementing 3 sorting algorithms:

* __Insertion Sort__
<br /> Run with following command:
  ```
  python3 insertion_sort.py
  ```
* __Selection Sort__
<br /> Run with following command:
  ```
  python3 selection_sort.py
  ```
* __Bubble Sort__
<br /> Run with following command:
  ```
  python3 bubble_sort.py
  ```

For each algorithm, the inputs are: A[5], B[10], C[2^16]

### Benchmarks

1. System Specifications:
   1. CPU: Apple M1 Pro
   2. RAM: 16 GB
   3. OS: MacOS Sonoma 14.0
   4. Python version: 3.9.7
2. The time taken to sort each array is measured using the `time` command in Linux.
   * __Insertion Sort__
     * A[5]: 6.91e-06 s
     * B[10]: 5.96e-06 s
     * C[2^16]: 80.02 s
   * __Selection Sort__
     * A[5]: 3.09e-05 s
     * B[10]: 2.59e-05 s
     * C[2^16]: 84.58 s
   * __Bubble Sort__
     * A[5]: 2.88e-05 s
     * B[10]: 2.09e-05 s
     * C[2^16]: 181.28 s


3. The memory usage is measured using tracemalloc, which is a built-in Python module that measures the size of the memory blocks allocated to the program. Only measures the memory used by objects.
This metric does not include the memory used by the array itself, since it is irrelevant to the algorithm. However, every time memory is allocated withing the algorithm, it is measured.
The usage of tracemalloc is only shown in insertion_sort.py, but the same method was used for all 3 algorithms.
Because tracemalloc interferes with the time measurement (that is increases the time consumed to execute the sort algorithm, the two measurement were done separately.
   * __Insertion Sort__
     * A[5]: 96 B
     * B[10]: 96 B
     * C[2^16]: 152 B
   * __Selection Sort__
     * A[5]: 144 B
     * B[10]: 144 B
     * C[2^16]: 284 B
   * __Bubble Sort__
     * A[5]: 144 B
     * B[10]: 144 B
     * C[2^16]: 284 B