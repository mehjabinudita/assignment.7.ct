def chop(lst):
    """Remove the first and last elements of the list."""
    if len(lst) >= 2:
        lst.pop(0)
        lst.pop(-1)
    else:
        print("List has less than 2 elements. Cannot remove first and last.")
    return None

def middle(lst):
    """Return a new list containing all elements except the first and last elements."""
    if len(lst) < 3:
        return []  
    return lst[1:-1]


my_list = [1, 2, 3, 4, 5]
print("my list before call chop function =>", my_list)

chop(my_list)
print("my list after call chop function =>", my_list)

new_list = middle(my_list)
print("new list after call middle function =>", new_list)
