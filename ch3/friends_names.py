friends_names = ["jaison", "edwin", "patrick", "larry", "tito", "henry", 
                 "garrett", "joel"]

print("My friends names are, in no particular order:")
for index, name in enumerate(friends_names):
  friends_out = f"{index + 1}. {name} is a great friend!"
  print(friends_out)
