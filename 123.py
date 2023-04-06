my_list = [17,0,2,14,10,8,13,13,14,4]

list1 = [(idx,el) for idx, el in enumerate(my_list) if el >= 0 and el <= 8]
print(list1)