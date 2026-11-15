secretno: int = 45
guess = int(input("Guess the secret number: "))
if guess < secretno:
    print("HIGHER")
elif guess > secretno:
    print("LOWER")
else:
    print("CORRECT")
