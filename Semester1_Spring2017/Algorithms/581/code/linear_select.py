import sys


def insertion_sort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue


def read_in_list_l(input_file, n):
    l = []
    i = 0
    with open(input_file, 'r') as f:
        for line in f:
            for num in line.split():
                i += 1
                l.append(int(num))
                if i == n:
                    return l


# This function implements linear-time selection using the
# median-of-medians method.
def linear_select(L, n, k):
    print "k: ", k
    print "n: ", n
    print "L: ", L

    r = 5
    sorting_n = 5
    num_groups = n/r
    last_group_size = n % r

    for i in range(0, num_groups-1):
        group = L[i*r:i*r+5]
        insertion_sort(group)
        L[i*r:i*r+5] = group

    group = L[(num_groups-1)*r:]
    insertion_sort(group)
    L[(num_groups*r)-1:] = group

    print L

    return L[0]


# linear_select input_file k n
def main():
    # get arguments
    input_file = sys.argv[1]
    k = int(sys.argv[2])
    n = int(sys.argv[3])
    L = read_in_list_l(input_file, n)

    # Error check
    if L is None:
        print "Not enough elements in file for that n."
        return

    kth_smallest = linear_select(L, n, k)
    print kth_smallest
    return

if __name__ == "__main__":
    main()

