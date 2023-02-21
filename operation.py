def find_comm_ele(lst1, lst2):
    comm_ele = []
    for item in lst1:
        if item in lst2:
            comm_ele.append(item)
    return comm_ele
