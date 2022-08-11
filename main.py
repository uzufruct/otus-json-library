from src.Library import Library

obj = Library('data/books.csv')
obj.load_readers('data/users.json')
obj.distribute('data/result.json')
