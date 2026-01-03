import random

def game(ch, gc):
    while gc < ch:
        gc += 1
        guess = int(input('Enter your guess: '))
        if guess == num:
            print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
            break
        elif gc >= ch and guess != num:
            print(f'Sorry! The number was {num}. Better luck next time.')
        elif guess > num:
            print('Too high! Try a lower number.')
        elif guess < num:
            print('Too low! Try a higher number.')
t = "Number Guessing Game"
w = 50
ct = t.center(w)
print(ct)

while True:
    print("\nChoose your Difficulty:")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")
    print("4) Exit")
    choice = int(input("\nEnter the corresponding number to your choice: "))
    if choice == 1:
        print("\nYou have 7 chances to guess the number between 0 and 20. Let's start!")
        num = random.randint(0, 20)
        ch = 7
        gc = 0
        game(ch, gc)
    elif choice == 2:
        print("\nYou have 6 chances to guess the number between 0 and 40. Let's start!")
        num = random.randint(0, 40)
        ch = 6
        gc = 0
        game(ch, gc)
    elif choice == 3:
        print("\nYou have 5 chances to guess the number between 0 and 100. Let's start!")
        h=100
        num = random.randint(0, 40)
        ch = 5
        gc = 0
        game(ch, gc)
    elif choice == 4:
        print("\nThanks for playing! Goodbye!")
        break
    else:
        print("\nPlease enter a valid option (1–4).")
    
