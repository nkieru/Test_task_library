from functions import record_data, last_id
import json


class Book:

    def __init__(self, title: str, author: str, year: int, status: bool = True):
        id_book = last_id() + 1
        self.id = id_book
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def record(self):
        try:
            with open('Books.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []
        data.append(self.__dict__)
        record_data(data)

    def __str__(self):
        return (f'\nID: {self.id} \nНазвание: {self.title}\nАвтор: {self.author} \nГод: {self.year}\n'
                f'Статус: {'В наличии' if self.status else 'Выдана'}\n')
