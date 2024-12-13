import json


class Book:

    def __init__(self, title: str, author: str, year: int, status: bool = True):
        id_book = last_id() + 1
        self.id = id_book
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return (f'\nID: {self.id} \nНазвание: {self.title}\nАвтор: {self.author} \nГод: {self.year}\n'
                f'Статус: {'В наличии' if self.status else 'Выдана'}\n')


def last_id():
    try:
        with open('../Books.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            id_last = data[-1]['id']

    except (FileNotFoundError, ValueError, IndexError):
        id_last = 0

    return id_last
