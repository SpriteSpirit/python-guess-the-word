from random import sample
import requests


def load_random_word(json_link: str, class_name: str):
    """Получает список слов с внешнего ресурса, выбирает случайное слово,
    создает экземпляр класса BasicWord и возвращает его"""

    response = requests.get(json_link)
    json_data = response.json()

    class_obj = getattr(__import__("basic_word"), class_name)

    random_word = sample(json_data, 1)[0]
    word_object = class_obj(random_word['word'], random_word['subwords'])

    return word_object


def get_text_info(text: str = "", members: int = 2) -> None or str:
    """Выводит указанный текст в соответствии с ролями"""

    progr = "Программа:"
    user = "Пользователь:"

    if members == 1:
        print(f"{progr} {text} ")
    elif members == 2:
        print(f"{progr} {text} ")
        user = input(f"{user} ")
        return user


def get_stats(guessed_words: int) -> None:
    """Выводит статистику по окончанию игры (использовано стоп-слово или отгаданы все слова)"""

    get_text_info(f"Игра завершена, вы угадали {guessed_words} слов(-а)!", 1)
    get_text_info("Thanks for playing!", 1)
    input("Press any key to exit...")
    quit()
