list = [0,2,3,4,5,6,7,8,9,-6,-5,-4,-3,-2,-1]

'''
List slicing just extracts the elements of the input list, 
and not modifies or trims the input list.
'''
# return last two elements of list
print("last two elements:", list[-2:])

# return all elements of list except last two elements
print("all elements except last two:",list[:-2])

# reverse the order of elements
print("elements in reverse order:", list[::-1])

# original list is unmodified
print("original list:",list)