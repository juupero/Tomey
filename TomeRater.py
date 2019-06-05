class TomeRater:
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {}!".format(email))

    def add_user(self, name, email, user_books = None):
        user = User(name, email)
        self.users[email] = user
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users:
            print(user)

    def most_read_book(self):
        max_read_count = 0
        most_popular_books = [] # In case there are more than one book with as many reads
        for book in self.books:
            if self.books[book] > max_read_count:
                del most_popular_books[:] # Empty the list in case there is a book with more reads
                max_read_count = self.books[book]
                most_popular_books.append(book)
            elif self.books[book] == max_read_count:
                most_popular_books.append(book)
        return most_popular_books

    def highest_rated_book(self):
        highest_rating = 0
        best_rated_books = [] # In case there are more than one book with the same rating
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                del best_rated_books[:] # Empty the list in case there is a book with better rating
                highest_rating = book.get_average_rating()
                best_rated_books.append(book)
            elif book.get_average_rating() == highest_rating:
                best_rated_books.append(book)
        return best_rated_books

    def most_positive_user(self):
        highest_positivity = 0
        kindest_users = [] # In case there are more than one user with the same positivity rating
        for email in self.users:
            user = self.users[email]
            if user.get_average_rating() > highest_positivity:
                del kindest_users[:] # Empty the list in case there is a book with a better rating
                highest_positivity = user.get_average_rating()
                kindest_users.append(email)
            elif user.get_average_rating() == highest_positivity:
                kindest_users.append(email)
        return kindest_users

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {} has been updated!".format(self.name))

    def __repr__(self):
        print("User {}, email: {}, books read: {}".format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def get_average_rating(self):
        user_ratings = []
        for book in self.books:
            if self.books[book] is not None:
                user_ratings.append(self.books[book])
        average_rating = sum(user_ratings) / len(user_ratings)
        return average_rating

    def read_book(self, book, rating = None):
        self.books[book] = rating

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __repr__(self):
        return "{}".format(self.title)

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Book {}'s ISBN has been updated!".format(self.isbn))

    def add_rating(self, rating):
        if type(rating) is int and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        book_ratings = []
        for rating in self.ratings:
            if rating is not None:
                book_ratings.append(rating)
        average_rating = sum(book_ratings) / len(book_ratings)
        return average_rating


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{} - a {} manual on {}".format(self.title, self.level.upper(), self.subject)






