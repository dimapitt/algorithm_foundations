import merge_sort as ms  # Imported my merge_sort as a default sorter for select
import math
import copy


def select(array_in, sort_func=ms.sort, batch_size=5, out_ops=False):
    #  Split array into batch_size's
    array = copy.deepcopy(array_in)  # Because we don't want to mess with the input
    goal_ind = math.ceil(len(array)/2)-1
    out, operations = do_select(array, sort_func, batch_size, goal_ind)

    if out_ops:
        return out, operations
    else:
        return out


def do_select(array, sort_func, batch_size, goal_ind, ops=0):
    med_value, ops = median_of_medians(array, sort_func, batch_size, ops=ops)  #Get median of medians
    med_loc = array.index(med_value)
    array, pivot_pos = partition(array, med_loc)

    if pivot_pos == goal_ind:
        ops += 1  # 1 operation if we get here
        selected_val = array[pivot_pos]
    elif pivot_pos < goal_ind:
        ops += 2  # 2 operations if we get here
        array = array[pivot_pos+1:]  # keep vals to the right of pivot pos
        goal_ind = goal_ind-pivot_pos-1
        selected_val, ops = do_select(array, sort_func, batch_size, goal_ind, ops=ops)
    else:
        ops += 2  # Still 2 operations
        array = array[:pivot_pos]  # keep vals to the left of pivot pos
        selected_val, ops = do_select(array, sort_func, batch_size, goal_ind, ops=ops)

    return selected_val, ops


def median_of_medians(array, sort_func, batch_size, ops=0):
    # Add operations from each merge sort
    medians = []
    array_len = len(array)
    for batch_start in range(0, array_len, batch_size):
        c_array = array[batch_start:min(batch_start + batch_size, array_len)]
        c_array_len = len(c_array)
        c_sorted, new_ops = sort_func(c_array, out_ops=True)
        ops = new_ops+ops   # Add operations from merge sort
        medians.append(c_sorted[math.ceil(c_array_len/2)-1])
    if len(array) > 1:
        return median_of_medians(medians, sort_func, batch_size, ops=ops)
    else:
        return array[0], ops


def partition(array, pivot_ind):
    # Assume Partition is free
    l_pivot = []
    r_pivot = []
    pivot_val = array[pivot_ind]  # Get pivot from array
    array.pop(pivot_ind)  # Remove pivot from array
    for val in array:
        if val > pivot_val:
            r_pivot.append(val)
        else:
            l_pivot.append(val)
    out_array = l_pivot+[pivot_val]+r_pivot  # concatenate left array, pivot, and right array
    pivot_pos = len(l_pivot)
    return out_array, pivot_pos


