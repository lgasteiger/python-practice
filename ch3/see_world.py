def print_list(curr_list):
    """prints the current list elements in the list 'curr_list'"""
    for index, place in enumerate(curr_list):
        output_message = f"{index + 1}. {place.title()}"
        print(output_message)
    # end for...in
# end print_list(curr_list)
        
places_to_visit = ['paris', 'london', 'berlin', 'norway', 'philippines']
print("Here is the unsorted places to visit list:")
print_list(places_to_visit)
print()

print("Here is the temporarily sorted places to visit list:")
sorted_list = sorted(places_to_visit)
print_list(sorted_list)
print()

print("Here is the places to visit list after calling 'sorted()' ")
print_list(places_to_visit)
print()

print("Here is the original places to visit listed in reversed order:")
places_to_visit.reverse()
print_list(places_to_visit)
print()

print("Here is the original places to visit list reversed back to its initial order:")
places_to_visit.reverse()
print_list(places_to_visit)
print()

print("Here is the place to visit list sorted permanently:")
places_to_visit.sort()
print_list(places_to_visit)
print()

print("Here is the places to see list sorted in reverse order:")
places_to_visit.sort(reverse=True)
print_list(places_to_visit)
print()
