import utils
from player import Player


def play(player_name: str) -> None:
    """
    Запускает игровой цикл:
    загрузка рандомного слова, создание игрока, проверка стоп-слова и верных ответов.
    Вывод статистики
    """
    # ------------create objects: word and player-------------- #
    word = utils.load_random_word("https://api.jsonserve.com/QgUZ0L", "BasicWord")
    player = Player(player_name)

    # ------------greeting player and game description-------------- #
    utils.get_text_info(f"Привет, {player_name}!", 1)
    utils.get_text_info(f"Составьте {word.count_subwords()} слов из слова {word.current_word.upper()}", 1)
    utils.get_text_info(f"Слова должны быть не короче {len(min(word.allowed_subwords))} букв", 1)
    utils.get_text_info("Чтобы закончить игру, угадайте все слова или напишите 'stop'", 1)

    answer = utils.get_text_info("Поехали, ваше первое слово?")

    # ------------count's variable and conditions variables for checking-------------- #
    last_count = 0
    stop = answer in ["stop", "стоп"]
    guessed_all = player.get_count_used_words() == word.count_subwords()

    # ------------game loop-------------- #
    while all([not stop, not guessed_all]):
        if stop:
            break
        elif word.check_allowed_subwords(answer) and not player.check_word_in_used(answer):
            player.add_used_word(answer)
            last_count += 1

            # ------------check last_count-------------- #
            if last_count == word.count_subwords():
                answer = utils.get_text_info("Верно!\n", 1)
            else:
                answer = utils.get_text_info("Верно!\n")
        elif word.check_allowed_subwords(answer) and player.check_word_in_used(answer):
            answer = utils.get_text_info("Уже использовано\n")
        elif not word.check_allowed_subwords(answer):
            answer = utils.get_text_info("Неверно\n")

        # ------------update answers-------------- #
        stop = answer in ["stop", "стоп"]
        guessed_all = player.get_count_used_words() == word.count_subwords()

    # ------------display stats-------------- #
    utils.get_stats(player.get_count_used_words())


# ------------get user_name and play the game-------------- #
user_name = utils.get_text_info("Введите имя игрока")
play(user_name)
