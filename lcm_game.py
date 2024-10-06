import random
import math
from functools import reduce
from engine import run_game

def lcm(a, b):
    """Функция для вычисления НОК двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    """Функция для вычисления НОК нескольких чисел."""
    return reduce(lcm, numbers)

def play_lcm_game(name):
    n = 3  
    for _ in range(n):
        numbers = [random.randint(1, 20) for _ in range(3)]
        
        print(f"Вычислите НОК для следующих чисел: {numbers}")
        
        correct_answer = lcm_multiple(numbers)
        
        while True: 
            try:
                user_answer = int(input("Ваш ответ: "))
            except ValueError:
                print("Пожалуйста, введите целое число.")
                continue  
            
            if user_answer == correct_answer:
                print("Правильно! Вы молодец!")
                break  
            else:
                print(f"Неправильно. Правильный ответ: {correct_answer}.")
                print(f"'{user_answer}' — это неправильный ответ ;(. Попробуйте снова.")

    print(f"Поздравляю, {name}! Вы выиграли в игре на НОК!")

if __name__ == "__main__":
    play_lcm_game("Player")