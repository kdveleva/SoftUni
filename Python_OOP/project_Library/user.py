from project_Library.library import Library


class User:

    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author: str, book_name: str, days_to_return: int,
                 library: Library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            library.rented_books[self.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        for u, b_t in library.rented_books.items():
            for b, t in b_t.items():
                if b == book_name:
                    return f'The book "{book_name}" is already rented and will be ' \
                           f'available in {library.rented_books[u][book_name]} days!'

    def return_book(self, author: str, book_name: str, library: Library):
        if book_name not in self.books:
            return f"{self.username} doesn't have this book in his/her records!"

        library.books_available[author].append(book_name)
        del library.rented_books[self.username][book_name]
        del self.books[self.books.index(book_name)]

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"
























