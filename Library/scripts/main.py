from src.functions import *


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


def to_list():
    while True:
        books_list = input('Введите 6, чтобы вернуться к списку книг или любой символ для возвращения к началу: ')
        if books_list == '6':
            list_of_books()
        else:
            greet()
            print(ask())


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
