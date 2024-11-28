import json


def last_id():
    try:
        with open('Books.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            id_last = data[-1]['id']

    except FileNotFoundError:
        id_last = 0

    except ValueError:
        id_last = 0

    except IndexError:
        id_last = 0

    return id_last


def load_data():
    with open('Books.json', 'r', encoding='utf-8') as file:
        books = json.load(file)
        data = []
        for b in books:
            data.append(b)
        return data


def record_data(data):
    with open('Books.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def id_search(search_id, data):
    books_id = [book['id'] for book in data]
    if search_id not in books_id:
        return True


def show_book(book):
    if book['status']:
        status = 'В наличии'
    else:
        status = 'Выдана'
    print('\n', 'ID: ', book['id'], '\n', 'Название: ', book['title'], '\n', 'Автор: ', book['author'], '\n',
          'Год: ', book['year'], '\n', 'Статус: ', status, '\n')
