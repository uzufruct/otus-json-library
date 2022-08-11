import csv
import json
import numpy


class Library:

    def __init__(self, src):
        self.readers = None
        with open(src, "r") as file:
            reader = csv.reader(file)
            self.header = next(reader)
            self.lib = [row for row in reader]

    def load_readers(self, src):
        with open(src, "r") as file:
            self.readers = json.loads(file.read())

    @property
    def readers_count(self):
        return len(self.readers)

    def distribute(self, src):
        refs = [{"name": person["name"],
                 "gender": person["gender"],
                 "address": person["address"],
                 "age": person["age"],
                 "books": []
                 } for person in self.readers]

        # split books array
        arr = numpy.array_split(numpy.array(self.lib), self.readers_count)
        distr_books = [a.tolist() for a in arr]

        # distribute with complexity O(N * log N) (???)
        for ref, books in zip(refs, distr_books):
            books_list = list()
            for book in books:
                books_list.append({
                    "title": book[0],
                    "author": book[1],
                    "pages": book[3],
                    "genre": book[2]
                })
            ref["books"] = books_list

        with open(src, "w") as file:
            rows = json.dumps(refs, indent=4)
            file.write(rows)
