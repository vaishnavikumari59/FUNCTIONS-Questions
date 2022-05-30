# Sample_List : [1,2,3,3,3,3,4,5]
# Unique_List : [1, 2, 3, 4, 5]
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list([1,2,3,3,3,3,4,5]))