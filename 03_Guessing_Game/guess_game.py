secret_name = "sidorela"
guess = ""
guess_count = 0
out_of_guesses = False
guess_limit = 3

while guess != secret_name and not(out_of_guesses):
    if guess_count < guess_limit :
        guess = input("Enter guess: ")
        guess_count +=1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lost!s You are our of guesses")
else:
    print("You win")