from exceptions import *
from functions import load_data, show_book


def title_search():
    data = load_data()
    search_title = input('Введите название книги: ')
    books_title = [book['title'] for book in data]
    if search_title in books_title:
        data = [d for d in data if d.get('title') == search_title]
        count = 0
        print(f'\nКниги найдены: ')
        for book in data:
            count += 1
            show_book(book)
        print(f'Книг с названием {search_title}: {count} шт\n')
    else:
        print('Нет книги с таким названием')


def author_search():
    data = load_data()
    search_author = input('Введите имя автора: ')
    books_author = [book['author'] for book in data]
    if search_author in books_author:
        data = [d for d in data if d.get('author') == search_author]
        count = 0
        print(f'\nКниги найдены: ')
        for book in data:
            count += 1
            show_book(book)
        print(f'Книг автора {search_author}: {count} шт\n')
    else:
        print(f'Нет книг автора {search_author}')


def year_search():
    data = load_data()
    search_year = int(input('Введите год: '))
    books_year = [book['year'] for book in data]
    if search_year in books_year:
        data = [d for d in data if d.get('year') == search_year]
        count = 0
        print(f'\nКниги найдены: ')
        for book in data:
            count += 1
            show_book(book)
        print(f'Книг {search_year} года: {count} шт\n')
    else:
        print(f'Нет книг {search_year} года')
