class TomeRater:
    def __init__(self):
        self.users = {} # key: user’s email, value: corresponding User object
        self.books = {} # key: Book object, value: the number of Users that have read it

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise ValueError("Invalid Name, it has to be a string.")
        self._name = name

    def create_book(self, title, isbn, price = None):
        return Book(title, isbn, price)

    def create_novel(self, title, author, isbn, price = None):
        return Fiction(title, author, isbn, price)

    def create_non_fiction(self, title, subject, level, isbn, price = None):
        return Non_Fiction(title, subject, level, isbn, price)

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
        most_popular_books = []
        for book in self.books:
            if self.books[book] > max_read_count:
                del most_popular_books[:]
                max_read_count = self.books[book]
                most_popular_books.append(book)
            elif self.books[book] == max_read_count:
                most_popular_books.append(book)
        return most_popular_books

    def highest_rated_book(self):
        highest_rating = 0
        best_rated_books = []
        for book in self.books:
            if book.get_average_rating() > highest_rating:
                del best_rated_books[:]
                highest_rating = book.get_average_rating()
                best_rated_books.append(book)
            elif book.get_average_rating() == highest_rating:
                best_rated_books.append(book)
        return best_rated_books

    def most_positive_user(self):
        highest_positivity = 0
        kindest_users = []
        for email in self.users:
            user = self.users[email]
            if user.get_average_rating() > highest_positivity:
                del kindest_users[:]
                highest_positivity = user.get_average_rating()
                kindest_users.append(email)
            elif user.get_average_rating() == highest_positivity:
                kindest_users.append(email)
        return kindest_users

    def get_n_most_expensive_books(self, n):
        amount_of_books = len(self.books)
        if amount_of_books >= n:
            book_price_list = [(book, book.get_price()) for book in self.books]
            sorted_book_price_list = sorted(book_price_list, key=lambda tup: tup[1], reverse=True)
            return sorted_book_price_list[:n]
        print("You have requested more books than there is ({}) in book TomeRater.".format(amount_of_books))

    def get_worth_of_user(self, user_email):
        if user_email in self.users:
            user_object = self.users[user_email]
            user_book_worth = sum([key.get_price() for key in user_object.books])
            return (user_email, user_book_worth)
        print("User {} has not been registered to TomeRate".format(user_email))

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def __repr__(self):
        print("User {}, email: {}, books read: {}".format(self.name, self.email, len(self.books)))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) is not str:
            raise ValueError("Invalid Name, it has to be a string.")
        self._name = name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if type(email) is not str or "@" not in email:
            raise ValueError("Invalid Email, it has to be a string with an '@'.")
        self._email = email

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("User {} has been updated!".format(self.name))

    def get_average_rating(self):
        user_ratings = [self.books[book] for book in self.books if self.books[book] is not None]
        try:
            average_rating = sum(user_ratings) / len(user_ratings)
        except ZeroDivisionError:
            print("There are no books with user ratings. Add some ratings and try again.")
        return average_rating

    def read_book(self, book, rating = None):
        self.books[book] = rating

class Book(object):
    def __init__(self, title, isbn, price):
        self.title = title
        self.isbn = isbn
        self.price = price
        self.ratings = []

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if type(title) is not str:
            raise ValueError("Invalid Title, it has to be a string.")
        self._title = title

    @property
    def isbn(self):
        return self._title

    @isbn.setter
    def isbn(self, isbn):
        if type(isbn) is not int or isbn < 0:
            raise ValueError("Invalid ISBN")
        self._isbn = isbn

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if type(price) is not int and type(price) is not float or price < 0:
            raise ValueError("Invalid price")
        self._price = price

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

    def get_price(self):
        return self.price

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Book {}'s ISBN has been updated!".format(self.isbn))

    def set_price(self, new_price):
        self.price = new_price
        print("Book {}'s price has been updated to {}!".format(self.title, self.price))

    def add_rating(self, rating):
        if type(rating) is int and 0 <= rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating, the rating was not added.")

    def get_average_rating(self):
        book_ratings = [rating for rating in self.ratings if rating is not None]
        try:
            average_rating = sum(book_ratings) / len(book_ratings)
        except ZeroDivisionError:
            print("There are no books with user ratings. Add some ratings and try again.")
        return average_rating

class Fiction(Book):
    def __init__(self, title, author, isbn, price):
        super().__init__(title, isbn, price)
        self.author = author

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if type(author) is not str:
            raise ValueError("Invalid Author, it has to be a string.")
        self._author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}".format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn, price):
        super().__init__(title, isbn, price)
        self.subject = subject
        self.level = level

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, subject):
        if type(subject) is not str:
            raise ValueError("Invalid Subject, it has to be a string.")
        self._subject = subject

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, level):
        if type(level) is not str:
            raise ValueError("Invalid Level, it has to be a string.")
        self._level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{} - a {} manual on {}".format(self.title, self.level.upper(), self.subject)
