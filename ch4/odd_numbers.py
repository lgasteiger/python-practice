import time

start_time = time.time()
odd_numbers = [i for i in range(1, 21, 2)]

for num in odd_numbers:
    output_message = f"an odd number between 1 and 20 inclusive is: {num}"
    print(output_message)
# end for

end_time = time.time()
time_taken = end_time - start_time
output_message = (
    f"the time it took to create the odd numbers between 1 and " +
    f"20 and print them is '{time_taken}' in seconds"
)
print(output_message)
