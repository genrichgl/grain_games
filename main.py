from progression_game import play_progression_game
from lcm_game import play_lcm_game
from engine import run_game

def main():
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print(f"Hello, {name}!")
    
    while True:
        print("\nВыберите игру:")
        print("1. Геометрическая прогрессия")
        print("2. Игра на нахождение НОК")
        print("3. Выход")
        
        choice = input("Ваш выбор (1-3): ")
        
        if choice == '1':
            run_game(lambda: play_progression_game(name))
        elif choice == '2':
            run_game(lambda: play_lcm_game(name))
        elif choice == '3':
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()