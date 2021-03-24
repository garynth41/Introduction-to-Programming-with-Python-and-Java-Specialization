def unique_list(l):
    """Returns a list of unique values from given list l."""

    x = []

    #iterate over provided list
    for a in l:
        #check if number is in new list
        if a not in x:
            #add it to new list
            x.append(a)

    return x

print(unique_list([1,2, 3, 3, 3, 3, 3, 4, 5]))
