import random

def number():
    nombre1 = int(input('Vous devez choisir entre deux nombre, choisissez le premier'))
    nombre2 = int(input('Vous devezentre deux nombres, choisissez le second'))
    return random.randint(nombre1, nombre2)

playing = True
while playing:
    number_range = number()
    winning = False
    number_try = 0
    while not true:
        number_try += 1

        guess_numbers = int(input('Choisissez un nombre entre les nombres que vous avez choisis'))

        if guess_numbers › number_range:
            print('Votre nombre est trop grand, choisissez un plus petit')
        elif guess_numbers< number_range:
            print('Votre nombre est trop petit, choisissez un plus grand')
        else:
            print('Vous avez fini en:', number_try)
            winning = True
    recommencer = input('Est-ce que vous voulez recommencer y')