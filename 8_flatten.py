# List Flattening
# Flatten a nested list, e.g., [1, [2, 3], [4, [5, 6]]] -> [1, 2, 3, 4, 5, 6].

# It uses recursion to go through all the levels of nesting.
def flatten_list(nested_list):
    flat_list = [] 


    for item in nested_list:
  
        if type(item) is list:
            for sub_item in flatten_list(item): 
                flat_list.append(sub_item)
        else:
            flat_list.append(item)
            
    return flat_list

my_nested_list = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

print('The original list: ', my_nested_list)

flattened_result = flatten_list(my_nested_list)

print('The list after removing nesting: ', flattened_result)
