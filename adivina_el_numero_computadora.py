import random

def guess(x):
  random_number = random.randint(1, x)
  guess = 0
  while guess != random_number:
    guess = int(input(f"Adivina un número entre 1 y {x}: "))
    if guess < random_number:
      print("Lo siento, adivina de nuevo. Demasiado bajo.")
    elif guess > random_number:
      print("Lo siento, adivina de nuevo. Demasiado alto.")

  print(f"Que bien, felicidades has adivinado el número {random_number} correctamente!")

guess(10)
