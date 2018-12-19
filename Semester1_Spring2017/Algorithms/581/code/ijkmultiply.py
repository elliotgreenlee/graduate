import time
import random
random.seed(1234)


def ijk_multiply(A, B):
    n = len(A)
    C = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            for k in xrange(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


def create_random_matrix(n):
    max_val = 1000  # I don't want to get Java / C++ into trouble ;-)
    matrix = []
    for i in range(n):
        matrix.append([random.randint(0, max_val) for el in range(n)])
    return matrix


if __name__ == "__main__":
    f = open("ijk_results.txt", 'w')
    for n in [1024, 2048]:
        total = 0
        f.write(str(n) + "\n")
        f.flush()
        print n
        for iterations in range(0, 5):
            A = create_random_matrix(n)
            B = create_random_matrix(n)

            start = time.time()
            C = ijk_multiply(A, B)
            end = time.time()
            expired = end - start
            total += expired

            f.write(str(expired) + "\n")
            f.flush()
        f.write(str(total / 5.0) + "\n")
        f.flush()
        # print_matrix(C)
