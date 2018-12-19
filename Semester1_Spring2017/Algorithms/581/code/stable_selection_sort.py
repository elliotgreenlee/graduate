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