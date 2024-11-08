my_list = [1,2,3,4,5]
my_list[4]=7
my_list.append(9)
my_list.insert(0,6)
my_list.remove(2)
result = my_list[2:5]
print(result)
for x in my_list:
    print(x)


new_list = my_list+[2,3,4]
print(new_list)
print(len(new_list))
print([x**3 for x in new_list])
print(new_list.sort())