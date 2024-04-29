import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)


def display_directory_structure(directory_path, indent=0):
    # Створення об'єкта Path для заданого шляху
    path = Path(directory_path)

    # Перевірка, чи шлях існує та чи є це директорія
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Шлях '{directory_path}' не існує або не є директорією.")
        return

    # Виведення назви поточної директорії
    print(" " * indent + Fore.BLUE + f"📁 {path.name}/")

    # Обхід всіх піддиректорій та файлів у поточній директорії
    for item in path.iterdir():
        # Виведення піддиректорій
        if item.is_dir():
            print(" " * (indent + 2) + Fore.CYAN + f"📁 {item.name}/")
            display_directory_structure(item, indent + 4)
        # Виведення файлів
        elif item.is_file():
            print(" " * (indent + 2) + Fore.GREEN + f"📄 {item.name}")


if __name__ == "__main__":
    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) != 2:
        print(Fore.RED + "Потрібно вказати шлях до директорії.")
        sys.exit(1)

    # Отримання шляху до директорії з аргументу командного рядка
    directory_path = sys.argv[1]

    # Виведення структури директорії
    display_directory_structure(directory_path)
