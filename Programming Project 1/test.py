from random import randint
import merge_sort
import selection
import statistics as s
import os
rand_array = x = [randint(0, 10000) for p in range(0, 100000)]
out = merge_sort.sort(rand_array)
array = [4,2,3,1]
sorted, operations = merge_sort.sort(array, out_ops=True)
print(sorted)
print(operations)

medsEst, operations = selection.select(rand_array, out_ops=True)
medsReal = s.median_low(rand_array)
print(medsEst)
print(medsReal)
print(operations)
print(len(rand_array))