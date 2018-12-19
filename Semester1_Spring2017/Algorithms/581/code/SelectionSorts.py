def stable_selection_sort(unsorted_list):

    for index in range(0, len(unsorted_list)):
        min_index = index
        min_number = unsorted_list[min_index][0]
        for i in range(index, len(unsorted_list)):
            if unsorted_list[i][0] < min_number:
                min_index = i
                min_number = unsorted_list[min_index][0]

        tmp = unsorted_list[min_index]
        unsorted_list.remove(unsorted_list[min_index])
        unsorted_list.insert(index, tmp)

    sorted_list = unsorted_list
    return sorted_list


def unstable_selection_sort(unsorted_list):

    for index in range(0, len(unsorted_list)):
        min_index = index
        min_number = unsorted_list[min_index][0]
        for i in range(index, len(unsorted_list)):
            if unsorted_list[i][0] < min_number:
                min_index = i
                min_number = unsorted_list[min_index][0]

        tmp = unsorted_list[index]
        unsorted_list[index] = unsorted_list[min_index]
        unsorted_list[min_index] = tmp

    sorted_list = unsorted_list
    return sorted_list


unsorted_list = [(8,"Vaughan, Ty"),
(25,"Bachstein, Matthew James-Robert"),
(33,"Xing, Kunyue"),
(21,"Zhou, Tong"),
(46,"Marshall, Tyler Eugene"),
(7,"Richmond, Stephen Lewis"),
(9,"Dimovska, Mihaela"),
(32,"Wilder, Nathan Paul"),
(28,"Van Wyk, Franco"),
(4,"Sherman, Isaac Ben"),
(41,"Smith, Jared Reid"),
(5,"Johnson, Corey Michael"),
(99,"Sun, Lijun"),
(86,"Li, Jiali (Jiali)"),
(62,"Vaccaro, Phil (Phil)"),
(26,"mike hare"),
(71,"Jackson III, Clarence Leon"),
(75,"Rao, Divyani"),
(42,"Rouleau, Gregory Paul"),
(44,"Soleman, Sharon Anna (Anna)"),
(41,"Smith, Jared (Jared M. Smith)"),
(96,"Li, Jiangnan"),
(88,"Brown, Kris Allen"),
(17,"Greenlee, Elliot Davis"),
(43,"Vidineyev, Arthur Konstantinovich"),
(35,"Messing, Andrew Kenneth"),
(85,"Offor, Elvis Chukwunonso"),
(29,"Dawes, Kristen Michelle"),
(36,"Cao, Qinglei"),
(54,"Wyer, Austin R"),
(61,"Tooley, Par")]


unsorted_list1 = list(unsorted_list)
unsorted_list2 = list(unsorted_list)

print "unsorted list:", unsorted_list1
print "stable sorted list:", stable_selection_sort(unsorted_list1)
print "unstable sorted list:", unstable_selection_sort(unsorted_list2)

