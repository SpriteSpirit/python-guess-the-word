class BasicWord:
    def __init__(self, current_word: str, allowed_subwords: list):
        self.current_word = current_word
        self.allowed_subwords = allowed_subwords

    def check_allowed_subwords(self, answer: str) -> bool:
        """Проверяет введенное слово в списке допустимых подслов"""

        return True if len(answer) >= 3 and answer in ''.join(self.allowed_subwords) else False

    def count_subwords(self) -> int:
        """Считает количества подслов"""

        return len(self.allowed_subwords)

    def __repr__(self) -> str:
        """Возвращает информацию об объекте в строковом представлении"""

        return f"{self.current_word}"

