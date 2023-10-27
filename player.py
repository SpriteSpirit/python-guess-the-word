class Player:
    def __init__(self, name: str):
        self.name = name
        self.used_words = []

    def get_count_used_words(self) -> int:
        """Считает количество использованных слов"""

        return len(self.used_words)

    def add_used_word(self, word: str) -> None:
        """Добавляет слова в 'использованные слова'(used_words)"""

        self.used_words.append(word)

    def check_word_in_used(self, word: str) -> bool:
        """Проверяет использование данного слова до этого"""

        return word in self.used_words

    def __repr__(self) -> str:
        """Возвращает информацию об объекте в строковом представлении"""

        return f"{self.name}"
