# Co the dung  ''' ''' de chua dau ' va dau "
# Co the dung  ''' ''' de xuong dong trong chuoi

print('''Hello
"Im" 'Long'
''')

# Slicing

list = [1, 2, 3, 4, 5]
# [start:stop:step]
'''
print(list[0])
print(list[0:3])
print(list[0:3:2])
print(list[:2])
'''

# Chèn 1 phần tử start==stop
'''
list[1:1] = {100}
list[4:4] = {2000}
list[4:4] = {500, 400, 200}
print(list)
'''

# Chèn đầu [:0]
'''
list[:0] = {100}
'''
# Chèn cuối [len(ds):]
#Xóa [:]
list[:] = [] # Xóa hết chuỗi
list[1:4] = [] # Xóa từ vị trí 1-3
print(list)