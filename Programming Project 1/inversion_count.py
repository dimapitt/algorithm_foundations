
def count(array, ratio_out=False):  # Dumb way to count inversions
    inv_count = 0
    max_inv = 0
    for i in range(len(array)):
        max_inv += i
        for j in range(i+1, len(array)):

            if array[i] > array[j]:
                inv_count += 1
    if ratio_out:
        return inv_count/max_inv  # return inversion ratio
    else:
        return inv_count  # return # of inversion
