from random import randint


name = input("Hello! What is your name?\n")

number = randint(1, 20)
print(f"Well, {name}, I am thinking of a number between 1 and 20.")


def guess_the_number(name, number):
    count = 0
    while True:
        guess = int(input("Take a guess.\n"))

        if guess > number:
            print("Your guess is too high")
            count += 1
        elif guess < number:
            print("Your guess is too low")
            count += 1
        else:
            print(f"Good job, {name}! You guessed my number in {count} guesses!")
            break


guess_the_number(name, number)
