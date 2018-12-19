def ackermans(m, n):
    if (m == 0):
       return n+1
    elif (m > 0 and n == 0):
       return ackermans(m - 1, 1)
    elif (m > 0 and n > 0):
       return ackermans(m - 1, ackermans(m, n - 1))
    
print ackermans(3, 4)