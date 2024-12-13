import json
from src.book import Book
from src.exceptions import *
import datetime


def load_data():
    try:
        with open('../Books.json', 'r', encoding='utf-8') as file:
            books = json.load(file)
            data = []
            for b in books:
                data.append(b)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not data:
        print('Нет книг в библиотеке. Добавьте книги.')
    return data


def record_data(data):
    with open('../Books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def show_book(data):
    if data:
        count = 0
        for book in data:
            count += 1
            if book['status']:
                status = 'В наличии'
            else:
                status = 'Выдана'
            print('\n', 'ID: ', book['id'], '\n', 'Название: ', book['title'], '\n',
                  'Автор: ', book['author'], '\n', 'Год: ', book['year'], '\n', 'Статус: ', status, '\n')
        print(f'Найдено книг: {count} \n')


def list_of_books():
    data = load_data()
    show_book(data)


def create():
    data = load_data()
    while True:
        try:
            title_input = input('Название книги: \n')
            title = title_input.capitalize()
            author_input = input('Автор книги: \n')
            author = author_input.capitalize()
            year = int(input('Год: \n'))
            if 1000 > year or year > datetime.date.today().year:
                raise WrongYearException()
        except WrongYearException as e:
            print(e)
            continue
        status = True
        book = Book(title, author, year, status)
        data.append(book.__dict__)
        record_data(data)
        print(f'\nКнига успешно добавлена: {book}')
        break


def delete_book():
    data = load_data()
    if data:
        search_id = int(input('Чтобы удалить книгу, введите ID: '))
        if not id_search(search_id, data):
            print('ID не найден')
        else:
            if confirm() is True:
                data = [d for d in data if d.get('id') != search_id]
                record_data(data)
                print(f'Книга с ID = {search_id} успешно удалена')


def change_status():
    data = load_data()
    if data:
        search_id = int(input('Введите ID книги: '))
        if not id_search(search_id, data):
            print('ID не найден')
        for book in data:
            if book['id'] == search_id:
                if book['status']:
                    status = 'В наличии'
                    new_status = 'Выдана'
                if not book['status']:
                    status = 'Выдана'
                    new_status = 'В наличии'
                print(f'Статус книги с ID={search_id}: {status}. \n')
                if confirm() is True:
                    book['status'] = False if book['status'] else True
                    print(f'Статус книги с ID={search_id} изменен на статус: {new_status}')
                record_data(data)


def confirm():
    print('Чтобы подтвердить изменения, введите 1: ')
    choice = input('')
    match choice:
        case '1': res_confirm = True
        case _: res_confirm = False, print('Изменения отменены')
    return res_confirm


def id_search(search_id, data):
    books_id = [book['id'] for book in data]
    if search_id in books_id:
        return True


def title_search():
    data = load_data()
    if data:
        search_title = (input('Введите название книги: ')).capitalize()
        books_title = [book['title'] for book in data]
        if search_title in books_title:
            data = [d for d in data if d.get('title') == search_title]
            show_book(data)
        else:
            print('Нет книги с таким названием')


def author_search():
    data = load_data()
    if data:
        search_author = (input('Введите имя автора: ')).capitalize()
        books_author = [book['author'] for book in data]
        if search_author in books_author:
            data = [d for d in data if d.get('author') == search_author]
            show_book(data)
        else:
            print(f'Нет книг автора {search_author}')


def year_search():
    data = load_data()
    if data:
        search_year = int(input('Введите год: '))
        books_year = [book['year'] for book in data]
        if search_year in books_year:
            data = [d for d in data if d.get('year') == search_year]
            show_book(data)
        else:
            print(f'Нет книг {search_year} года')
