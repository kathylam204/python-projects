import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        computer_guess = random.randint(low,high)
        feedback = input(f'Is {computer_guess} too high (h), too low (l), or correct (c)?')
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1
print(f'Congrats {computer_guess} is the correct number!')

computer_guess(500)
