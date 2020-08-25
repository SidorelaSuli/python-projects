friends = ["friend2", "friend2", "friend3", "friend4"]
lucky_numers = [ 3, 7, 8, 1]
friends.append("friend5") # appends element in the end of the list
print(friends)
friends.insert(1, "friend11") # adds element on index 1
print(friends)
friends.remove("friend11") # removed 1 element
print(friends)
#friends.clear() # deletes all the elements of the list
friends.pop() # pops/removes an element from the list (the last one)
print(friends)
print(friends.index("friend3")) # returns the index of an element, id it exists on the list
print(friends.count("friend3"))
friends.sort()
print(friends)

friends2 = friends.copy()
print(friends2)