BigIntegerMultiplication(A, B)
    reserve memory space of return array C
    for i in range(0, len(A)):
       Aplace = len(A) - i
       for j in range(0, len(B)):
           Bplace = len(B) - j
           mult = A[i] * B[j]
           tens = mult / 10
           ones = mult % 10
           cTens = Aplace + Bplace
           cOnes = cTens - 1
           C[len(C) - cOnes] += ones
           carry = C[len(C) - cOnes] / 10
           C[len(C) - cOnes] %= 10
           C[len(C) - cTens] += carry + tens
           carry = C[len(C) - cTens] / 10
           C[len(C) - cTens] %= 10
           C[len(C) - cTens - 1] += carry
           for k in range(0, len(C)):
              carry = C[len(C) - 1 - k] / 10
              C[len(C) - 1 - k] %= 10
              C[len(C) - 1 - k - 1] += carry
return sum