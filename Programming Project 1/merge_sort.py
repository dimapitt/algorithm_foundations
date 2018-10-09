import math  # Only for the floor function :)


def sort(array, out_ops=False):
    out, operations = do_sort(array)
    if out_ops:
        return out, operations
    else:
        return out


def do_sort(array, start_ops=0):  # main sort algo
    split = math.floor(len(array)/2)  # split the array into 2
    l_array = array[:split]
    r_array = array[split:]

    if len(l_array) > 1:  # If the left array is > length 1, we need to sort it
        l_sorted, start_ops = do_sort(l_array, start_ops=start_ops)
    else:
        l_sorted = l_array

    if len(r_array) > 1:  # If the left array is > length 1, we need to sort it
        r_sorted, start_ops = do_sort(r_array, start_ops=start_ops)
    else:
        r_sorted = r_array

    return merge(l_sorted, r_sorted, start_ops)  # Now that we're done sorting, let's merge


def merge(l_array, r_array, ops):  # Do merging here
    li = 0  # left index
    ri = 0  # right index
    out = []
    max_r = len(r_array)
    max_l = len(l_array)

    while li < max_l and ri < max_r:  # Keep going until one of the arrays are empty
        if l_array[li] < r_array[ri]:  # Append using right or left array?
            out.append(l_array[li])
            li += 1
            ops += 1
        else:
            out.append(r_array[ri])
            ri += 1
            ops += 1

    if li == len(l_array):  # Append the rest of the non-empty array
        out.extend(r_array[ri:])
    else:
        out.extend(l_array[li:])

    return out, ops  # return merged array
