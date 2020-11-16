import random
# import the random module so we can use its functions
# set a range for the random number to be guessed to be
min = 1
max = 20

# begin the main game loop, and continue it as long as the player wants to keep playing
tryAgain = True
while tryAgain is True:
    # generate the number
    number = random.randint(min, max)
    # set up the number of guesses they have left every time
    guessesLeft = 5
    correct = False
    attempts = 0
    # keep asking them to guess until they are correct or they run out of guesses
    while guessesLeft > 0 and correct is False:
        # ask them for an integer. If they don't provide an integer, ask them again.
        while True:
            try:
                guess = int(input(f"The number is between {min} and {max}. You have {guessesLeft} guesses left."))
                # this break statement exits out of the above while True loop, allowing them to proceed
                break
            except:
                print("Please type an integer.")
        # adjust the number of guesses left and number of attempts
        attempts += 1
        guessesLeft -= 1
        # check their guess against the number
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            correct = True
            print(f"Correct! It took you {attempts} tries")
    # if they fall out of the loop by running out of guesses, they will be told what the number was
    if correct is False:
        print(f"Sorry, the number was {number}")
    # ask if they want to play again. We just assume that an answer that isn't y/yes is a no
    # also convert their response to lowercase in case they use capital letters
    response = input("Try again? (y/n)").lower()
    if response == "y" or response == "yes":
        tryAgain = True
    else:
        tryAgain = False
