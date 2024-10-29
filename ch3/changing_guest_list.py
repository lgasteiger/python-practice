def print_guest_list():
    """displays the current guest list to the screen"""
    for guest in my_guest_list:
        guest_output = f"{guest.title()}, you are invited to the dinner at washington dc headquarters. please arrive before 2000 hrs."
        print(guest_output)
    #end for...in
        
    guest_list_count = f"the current number of guests is: {len(my_guest_list)}" 
    print(guest_list_count)
# end print_guest_list()

my_guest_list = ['george washington', 'john adams', 'thomas jefferson', 'bill clinton', 'barack obama']
print_guest_list()
print()

cannot_attend = "bill clinton"
my_guest_list.remove(cannot_attend)
my_guest_no_attend = f"the guest who cannot attend is: {cannot_attend.title()}"
print(my_guest_no_attend)
print_guest_list()
print()

my_guest_list.append('hillary clinton')
print_guest_list()
print()
