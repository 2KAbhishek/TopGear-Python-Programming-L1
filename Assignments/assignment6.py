#!/usr/bin/env python

list1 = [5, 6, 1, 2, 3, 4, 7, 8, 9, 10]
list2 = [15, 12, 11, 20, 13, 16, 17, 19, 18, 14]
list3 = [23, 30, 24, 25, 26, 28, 27, 29, 21, 22]
max_list = []
min_list = []

list1.sort()
list2.sort()
list3.sort()

for i in (list1, list2, list3):
    max_list.append(i[-1])
    max_list.append(i[-2])
    min_list.append(i[0])
    min_list.append(i[1])

print('Maxlist: ' + repr(max_list))
print('Average of Maxlist:', sum(max_list)/len(max_list))


print('Minlist is: ' + repr(min_list))
print('Average of minlist:', sum(min_list)/len(min_list))
