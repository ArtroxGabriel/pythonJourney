import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} to high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Numero correto: {guess}")

def execute():

    computer_guess(int(input("Enter a number: ")))
    print("You guessed correctly!")
