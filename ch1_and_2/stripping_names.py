# Name: Tests the approaches to removing white space in positions before, after,
#       and both before and after.
# Date: 2024-03-11
# Author: Leo G. Gasteiger

my_name = "Leo Genesis Gasteiger"
out_message = f"\n\nMy bio is full of resume info:\n\tName: {my_name}\n\tDOB: 1975-08-19\n\n"

print(out_message)

print(f"Use of lstrip() is: {out_message.lstrip()}")
print(f"Use of rstrip() is: {out_message.rstrip()}")
print(f"Use of strip() is: {out_message.strip()}")
