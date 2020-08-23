name = "Sidorela Suli"

#functions
print(name.lower())
print(name.upper())
print(name.upper().isupper())
print(name.lower().islower())
print(len(name)) # length of the string

print(name[0]) # print the first letter of the string
print(name[1]) # prints the second letter of the string, name[2] prints the third etc....

print(name.index("u")) # returns the index where a character is located
print(name.index("Suli")) # you can also pass as a parameter words
print(name.replace("Suli", "Surname")) # replases strings