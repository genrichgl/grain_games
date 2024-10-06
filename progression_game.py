import random
from engine import run_game

def generate_geometric_progression(length, start, ratio):
    return [start * (ratio ** i) for i in range(length)]

def hide_element(progression):
    index = random.randint(0, len(progression) - 1)
    hidden_value = progression[index]
    progression[index] = '..'
    return progression, hidden_value

def play_progression_game(name):
    n = 3  
    for _ in range(n):
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        ratio = random.randint(2, 5)
        
        progression = generate_geometric_progression(length, start, ratio)
        hidden_progression, hidden_value = hide_element(progression)
        
        print("Геометрическая прогрессия:")
        print(' '.join(map(str, hidden_progression)))

        while True:  
            try:
                user_guess = float(input("Какое число скрыто за '..'? "))
            except ValueError:
                print("Пожалуйста, введите число.")
                continue  
            
            if user_guess == hidden_value:
                print("Правильно! Вы угадали!")
                break  
            else:
                print(f"Неправильно. Скрытое число: {hidden_value}. Попробуйте снова.")

    print(f"Поздравляю, {name}! Вы выиграли в игре с прогрессией!")

if __name__ == "__main__":
    play_progression_game("Player")