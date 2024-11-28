from exceptions import *
from search import *
from functions import record_data, load_data, id_search, show_book
from book import Book
import datetime
import json


def create():
    while True:
        try:
            title = input('Название книги: \n')
            if title[0].islower():
                raise LowerTitleException()
            author = input('Автор книги: \n')
            if author[0].islower():
                raise LowerAuthorException()
            year = int(input('Год: \n'))
            if 1000 > year or year > datetime.date.today().year:
                raise WrongYearException()
        except (LowerTitleException, LowerAuthorException, WrongYearException, IndexError) as e:
            print(e)
            continue
        status = True
        book = Book(title, author, year, status)
        book.record()
        print(f'\nКнига успешно добавлена: {book}')
        to_list()


def delete_book():
    try:
        data = load_data()
        if not data:
            print('Список книг пуст')
        if data:
            search_id = int(input('Чтобы удалить книгу, введите ID: '))
            if id_search(search_id, data):
                print('ID не найден')
            else:
                data = [d for d in data if d.get('id') != search_id]
                record_data(data)
                print(f'Книга с ID = {search_id} успешно удалена')
    except (FileNotFoundError):
        print('Список книг пуст')


def change_status():
    data = load_data()
    search_id = int(input('Введите ID книги: '))
    if id_search(search_id, data):
        print('ID не найден')
    for book in data:
        if book['id'] == search_id:
            if book['status']:
                status = 'В наличии'
                new_status = 'Выдана'
            if not book['status']:
                status = 'Выдана'
                new_status = 'В наличии'
            print(f'Статус книги с ID={search_id}: {status}. \nЧтобы подтвердить изменение статуса, введите 8: ')
            choice = input('')
            match choice:
                case '8': book['status'] = False if book['status'] else True
                case _: to_list()
            record_data(data)
            print(f'Статус книги с ID={search_id} изменен на статус: {new_status}')


def list_of_books():
    try:
        with open('Books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
            books_count = 0
            for book in books:
                books_count += 1
                show_book(book)
            print(f'Всего книг: {books_count}\n\n')
    except (FileNotFoundError, json.JSONDecodeError):
        print('Книг не найдено')


def to_list():
    while True:
        books_list = input('Введите 6, чтобы вернуться к списку книг или любой символ для возвращения к началу: ')
        if books_list == '6':
            list_of_books()
        else:
            greet()
            print(ask())


def greet():
    print('\n')
    print('____________________________')
    print('       Библиотека           ')
    print('____________________________')
    print('Для продолжения работы введите код операции:'
          '\n1 добавление'
          '\n2 удаление'
          '\n3 поиск по названию'
          '\n4 поиск по автору'
          '\n5 поиск по году'
          '\n6 список всех книг'
          '\n7 изменение статуса')


def ask():
    while True:
        try:
            decision = int(input('Код: '))
            match decision:
                case 1: create()
                case 2: delete_book()
                case 3: title_search()
                case 4: author_search()
                case 5: year_search()
                case 6: list_of_books()
                case 7: change_status()
                case _: print('Введенного кода не существует')
        except ValueError:
            print('Введены неверные данные! ')
            to_list()
            continue
        to_list()


greet()
print(ask())
