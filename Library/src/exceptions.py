class WrongDataException(Exception):
    pass


class WrongYearException(WrongDataException):
    def __str__(self):
        return f'Неверно указан год'
