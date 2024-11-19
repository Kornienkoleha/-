import random

number = random.randint(1, 100)
guesses_left = 7
print("Я загадал число от 1 до 100. У вас 7 попыток.")

while guesses_left > 0:
    try:
        guess = int(input(f"Осталось {guesses_left} попыток. Введите ваше число: "))
        if guess < number:
            print("Слишком мало!")
        elif guess > number:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Вы угадали число {number} за {7 - guesses_left} попыток!")
            break
        guesses_left -= 1
    except ValueError:
        print("Введите целое число!")

if guesses_left == 0:
    print(f"Вы исчерпали все попытки. Загаданное число было {number}.")