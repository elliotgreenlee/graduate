SelectionSort(A)
    n = len(A)
    for i in range(0, n):
       smallestIndex = i
       smallestNum = A[i]
       for j in range(i, n):
           if A[j] < smallestNum:
              smallestNum = A[j]
              smallestIndex = j
       tmp = A[i]
       A[i] = A[smallestIndex]
       A[smallestIndex] = tmp
return A