import time
import math

test_slices = [
    'pizza', 'pasta', 'cannoli', 'banana bread', 'fetuccni', 'ravioli'
]

print("the first 3 items in the list are:")
for index, food in enumerate(test_slices[:3]) :
    food_output = f"{index + 1}. {food}"
    print(food_output)
# end for

print("\nthe middle three elements are:")
middle_idx = len(test_slices) / 2
middle_idx = math.floor(middle_idx)

if len(test_slices) > 2:
    for index, food in enumerate(test_slices[middle_idx - 1:middle_idx + 2]):
        food_output = f"{index + 1}. {food}"
        print(food_output)
    # end for
else:
    print("!!!!!error, list not large enough!!!!!")
# end if
    
print("\nthe last three elements of the list are:")
for index, food in enumerate(test_slices[-3:]):
    food_output = f"{index + 1}. {food}"
    print(food_output)
# end for
