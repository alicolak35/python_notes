
empty_list = [ ]
empty_list = [2, 3]
not_empty_list = empty_list.copy()
not_empty_list.insert(4, 5) # added to index 2
not_empty_list.insert(3, 4) # added to index 3 
#  list.insert(a, num) has same effect as list.append(a) where a >= len(list)  

# append() and extend()
list_a = [ 2, 3, 4]
list_b = [ 5, 6, 7]

list_a.append(4) 
list_a.extend(list_b) #adds elements of list_b to the end of list_a  

list_a.remove(4) #removes first occurrence

try:
    list_a.remove(1)
except ValueError as e:
    print(e)

list_a.pop()
try:
    list_a.pop(8)
except IndexError as e:
    print(e)

del list_b # removes the list object list_b
list_b = [ 5,6,7 ]
list_b.clear() #clears the list_b, can be reused

try:
    del list_a[6] #does not throw IndexError 
except IndexError as e:
    print(e)

a = 13