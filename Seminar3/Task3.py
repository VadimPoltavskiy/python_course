#Напишите программу для печати всех уникальных значений в словаре.
myDict =    [{"V": "S001"},
            {"V": "S002"}, 
            {"VI": "S001"},
            {"VI": "S005"}, 
            {"VII": "S005"}, 
            {"V": "S009"}, 
            {"VIII": "S007"}] 
#my_list =[]
#for i in range(len(myDict)):
#    my_list += myDict[i].values()
#print (set(my_list))


new_list =[]
for item in myDict:
    for values in item. values():
        new_list.append(values)

print(set(new_list))
print(new_list)