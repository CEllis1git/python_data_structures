"""
Function to convert a set of numbers to a list, sort it, and convert back to tuple.
"""

number_set = (4, -100, 8, 7, 1, 22, -1)

def convert_and_sort(number_set):
    number_list = list(number_set)
    number_list.sort()
    tuple_redux_sorted = tuple(number_list)
    return tuple_redux_sorted

print("Original number set is ", number_set)
print("Sorted number set is ", convert_and_sort(number_set))


