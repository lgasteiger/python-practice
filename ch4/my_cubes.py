import time

print("here is the list of cubes from 1 to 10 using a traditional for loop")
start_time = time.time()
cubes_for_loop = []
for c in range(1, 10):
    cubes_for_loop.append(c ** 3)
# end for
print(cubes_for_loop)
end_time = time.time()
time_taken = end_time - start_time
output_summary = (
    f"the time it took to create the list of cubes from 1 to 10 and print " +
    f"the list of cubes was: {time_taken}"
) # end output_summary
print(output_summary)
print()

print("here is the list of cubes from 1 to 10 using a list comprehension")
start_time = time.time()
cubes_list_comp = [value ** 3 for value in range(1, 10)]
print(cubes_list_comp)
end_time = time.time()
time_taken = end_time - start_time
output_summary = (
    f"the time it took to create the list of cubes from 1 to 10 and print " +
    f"the list of cubes was: {time_taken}"
) # end output_summary
print(output_summary)
print()
