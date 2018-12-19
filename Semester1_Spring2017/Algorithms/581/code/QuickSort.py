def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

def partition(unpartitioned_list, lowest, highest):
    pivot = unpartitioned_list[highest]
    print pivot
    print unpartitioned_list, lowest, highest
    i = lowest

    for j in range(lowest, highest - 1):
        if unpartitioned_list[j] <= pivot:
            tmp = unpartitioned_list[i]
            unpartitioned_list[i] = unpartitioned_list[j]
            unpartitioned_list[j] = tmp
            i += 1

    tmp = unpartitioned_list[highest]
    unpartitioned_list[highest] = unpartitioned_list[i]
    unpartitioned_list[i] = tmp

    return i


unpartitioned_list = [2,3,4,5,6,7,8,1]
lowest = 0
highest = len(unpartitioned_list) - 1

print "unpartitioned_list:", unpartitioned_list
print "partitioned_list:", partition(unpartitioned_list, lowest, highest)