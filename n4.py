my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
no_duplicate = [i for i in my_list if my_list.count(i) == 1 ]
print(no_duplicate)