import time

start_time = time.time()
#threes_multiples = list(range(3, 31, 3))
threes_multiples = [i for i in range(3, 31, 3)]
for n in threes_multiples:
    output_display = f"a multiple of three is: {n}"
    print(output_display)
# end for
end_time = time.time()

time_taken = end_time - start_time
output_summary = (
    f"the time it took to create the threes list and print it out was " +
    f"{time_taken} taken."
)
print(output_summary)
