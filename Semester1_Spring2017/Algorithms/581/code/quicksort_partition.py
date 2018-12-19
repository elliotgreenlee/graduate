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