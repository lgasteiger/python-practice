def print_guest_list(curr_guest_list):
    """displays the current guest list to the screen"""
    for index, guest in enumerate(curr_guest_list):
        guest_output = f"{index + 1}. {guest.title()}, you are invited to the dinner at washington dc headquarters. please arrive before 2000 hrs."
        print(guest_output)
    #end for...in
        
    guest_list_count = f"the current number of guests is: {len(curr_guest_list)}" 
    print(guest_list_count)
# end print_guest_list()
    
def add_to_middle(curr_guest_list):
    """adds an element to the middle of the current guest list"""
    middle_idx = round(len(curr_guest_list) / 2)
    curr_guest_list.insert(middle_idx, 'al gore')
# end add_to_middle()

my_guest_list = ['george washington', 'john adams', 'thomas jefferson', 'bill clinton', 'barack obama']
print_guest_list(my_guest_list)
print()

cannot_attend = "bill clinton"
my_guest_list.remove(cannot_attend)
my_guest_no_attend = f"the guest who cannot attend is: {cannot_attend.title()}"
print(my_guest_no_attend)
print_guest_list(my_guest_list)
print()

my_guest_list.append('hillary clinton')
print_guest_list(my_guest_list)
print()

print("hello everyone, i found a bigger table, and i am able to invite more attendees!")
my_guest_list.insert(0, 'michelle obama')
# my_guest_list.insert(0, 'barack obama')
print_guest_list(my_guest_list)
print()

add_to_middle(my_guest_list)
print_guest_list(my_guest_list)
print()

my_guest_list.append('the donald j. trump')
print_guest_list(my_guest_list)
