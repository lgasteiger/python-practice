import time

one_mill_elements = list(range(1,1000001))
output_mess = f"the first element in the one million list is {min(one_mill_elements)}"
print(output_mess)
output_mess = f"the last element in the one million list is {max(one_mill_elements)}"
print(output_mess)
output_mess = f"the sum of the elements is {sum(one_mill_elements)}"
print(output_mess)
print()

start_time = time.time()
one_mill_elem_timer = [i for i in range(1, 1_000_001)]
output_mess = f"the first element in the one million list is {min(one_mill_elem_timer)}"
print(output_mess)
output_mess = f"the last element in the one million list is {max(one_mill_elem_timer)}"
print(output_mess)
output_mess = f"the sum of the elements is {sum(one_mill_elem_timer)}"
print(output_mess)
end_time = time.time()
time_taken = end_time - start_time
output_mess = f"the time it took me to create a list of a million elements and sum them is {time_taken} in seconds"
print(output_mess)
print()
