import time

def printout_data(list_in_ques):
    """this function prints the elements of list 'list_in_quest'"""
    for index, elem in enumerate(list_in_ques):
        data_output = f"{index + 1}. {elem}"
        print(data_output)
    # end for
# end printout_data(list_in_ques)
    
def printout_summary(start_duration, end_duration):
    """this function prints time it takes in seconds to complete the task(s)"""
    time_taken = end_duration - start_duration
    summary_output = (
        f"the time taken to complete the tasks in seconds is {time_taken}"
    ) # end summary_output var
    print(summary_output)
# end printout_summary(start_duration, end_duration)

# tests the slice of the first 3 elements of the list
print("*****tests the slice of the first 3 elements of the list*****")
start_time = time.time()
players = ['charles', 'martina', 'michael', 'florence', 'eli', 'leo']
certain_players = players[0:3]
printout_data(certain_players)
end_time = time.time()
printout_summary(start_time, end_time)
print()

print("*****tests the slice of the range of elements from 1 to 3*****")
start_time = time.time()
certain_players = players[1:4]
printout_data(certain_players)
end_time = time.time()
printout_summary(start_time, end_time)
print()

print("*****tests the slice of the first four elements in the list*****")
start_time = time.time()
beginning_players = players[:4]
printout_data(beginning_players)
end_time = time.time()
printout_summary(start_time, end_time)
print()

print("*****tests the slice of the remaining list elements starting from the "
      "third element*****")
start_time = time.time()
players_to_end = players[2:]
printout_data(players_to_end)
end_time = time.time()
printout_summary(start_time, end_time)
print()

print("*****tests the slice of the last three list elements using the negative "
      "int approach*****")
start_time = time.time()
players_at_end = players[-3:]
printout_data(players_at_end)
end_time = time.time()
printout_summary(start_time, end_time)
print()

print("*****tests the looping through a list slice*****")
start_time = time.time()
for player in players[:3]:
    print(player.title())
# end for
end_time = time.time()
printout_summary(start_time, end_time)
print()
