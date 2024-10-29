friends_names = ["jaison", "edwin", "patrick", "larry", "tito", "henry", 
                 "garrett", "joel"]

print("My friends names are, in no particular order:")
for index, name in enumerate(friends_names):
  friends_output = f"{index + 1}. {name} is a great friend! I hope you are doing well!!"
  print(friends_output)
