#-----sort va sorted-----

ls = [10, 4, 6, 2, -2, -4, -11, 4, 7, 3, 1]

# # ls.sort()

# listed = sorted(ls)

# print(ls)

#-----list theo dieu kien-----

def key1(item):
    return (
        -abs(item), # Sap xep theo gia tri tuyet doi nhung giam dan
        item # Sap xep theo gia tri thuc
    )

# Tang +, giam -

newlist = sorted(ls, key=key1)

print(ls)
print(newlist)

# Coppy một list
# newlists = list[:]


