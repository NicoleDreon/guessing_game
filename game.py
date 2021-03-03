"""A number-guessing game."""
import random
tries = 0
x = random.randint(1, 100)
# print(.format(x))
# def random_number(x):
    
# from random import random_number

print('Hello, player')
name = input("What is your name?   ")
print(f"Hello, {name}")
# guess = input("Guess a number between 1 and 100?  ")

while True:
  guess = input("Your guess? ")
  try: guess = int(guess)
  except ValueError:
    print(f"{guess} is not a valid number, try again.")
    continue

  tries += 1

  if guess < 1 and guess > 100:
    print("Not a valid entry")

  if x > guess: 
    print("Your guess is too low, try again")

  elif x < guess:
    print("Your guess is too high, try again")

  else:
    print(f"Well done, {name}!")
    print(f"You found the number in {tries} tries!")
    break