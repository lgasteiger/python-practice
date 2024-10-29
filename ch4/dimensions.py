import time

start_time = time.time()
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
end_time = time.time()
time_taken = end_time - start_time
output_message = (
    f"the amt of time in seconds to create the python tuple and output it's " +
    f"contents to the display was {time_taken}\n"
) # end output_message
print(output_message)
