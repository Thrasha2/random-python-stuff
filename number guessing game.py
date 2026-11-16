    import random


    num = int(random.randint(1, 100)) # creates a random number between 1 and 100
    guess = -9999999 # initialize the input variable to a value that is not equal to num so that the while loop can start
    attempts = 0 #initialize the counter variable to count the number of attempts


    while num != guess:
        while guess < 1 or guess > 100: #checks if the input is between 1 and 100
            guess = int(input("Guess a number between 1 and 100:"))
            attempts = attempts + 1 #increment the counter variable by 1 for each attempt
        if guess < num: #if statements to check if the input is too low or too high
            guess = int(input("Too low! Try again."))
            attempts = attempts + 1 #increment the counter variable by 1 for each attempt
        elif guess > num:
            guess = int(input("Too high! Try again."))
            attempts = attempts + 1 #increment the counter variable by 1 for each attempt
    print("Congratulations! You guessed the number!") #if the input is equal to num, the loop ends and this message is printed
    print("it took you " + str(attempts) + " attempts to guess the number.") # prints the number of attepts it took to guess the number