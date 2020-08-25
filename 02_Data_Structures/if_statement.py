
is_male = False
is_tall = True
if is_male or is_tall: # conditions: and, or, not()
    print("You are either male or tall")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male and tall")
else:
    print("You are neither male not tall")