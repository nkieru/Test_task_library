class WrongDataException(Exception):
    pass


class LowerTitleException(WrongDataException):
    def __str__(self):
        return f'Название должно начинаться с заглавной буквы'


class LowerAuthorException(WrongDataException):
    def __str__(self):
        return f'Имя автора должно начинаться с заглавной буквы'


class WrongYearException(WrongDataException):
    def __str__(self):
        return f'Неверно указан год'
