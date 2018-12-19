RecursiveInsertionSort(list):
       if len(list) == 1:
           return list
    else:
        sorted = RecursiveInsertionSort(list[0:len(list)-1])
        An = list[len(list)-1]
        
        for i in range(0, len(sorted)):
            if An >= sorted[i]:
                sorted.insert(i+1, An)
            return sorted
    return sum
