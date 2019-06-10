from TomeRater import *
import unittest

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678, 22.6)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345, 23.5)
novel1.set_isbn(9781536831139)
book1.set_price(25)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452, 29.7)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938, 33.2)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010, 59.9)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000, 44.5)

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)

Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
Tome_Rater.print_catalog()
Tome_Rater.print_users()

print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
number_of_books = 3
print("{} of the most expensive books:".format(number_of_books))
print(Tome_Rater.get_n_most_expensive_books(number_of_books))
print("The total worth of a user's books:")
print(Tome_Rater.get_worth_of_user("alan@turing.com"))

#Tests for value validation
class TestCreateBookValues(unittest.TestCase):
    def test_invalid_price_raises_error(self):
        self.assertRaises(ValueError, Tome_Rater.create_non_fiction, "Automate the Boring Stuff", "Python", "beginner", 1929452, "")

    def test_invalid_isbn_raises_error(self):
        self.assertRaises(ValueError, Tome_Rater.create_non_fiction, "Automate the Boring Stuff", "Python", "beginner", "1929452", 54)

class TestAddUserValues(unittest.TestCase):
    def test_invalid_name_raises_error(self):
        self.assertRaises(ValueError, Tome_Rater.add_user, 300, "alan@turing.com")

    def test_invalid_email_raises_error(self):
        self.assertRaises(ValueError, Tome_Rater.add_user, "Alan Turing", "noemailchar")

class TestMostExpensiveBook(unittest.TestCase):
    def test_equal_list_length(self):
        self.assertEqual(len(Tome_Rater.get_n_most_expensive_books(3)), 3)

    def test_too_many_books_return_none(self):
        self.assertIsNone(Tome_Rater.get_n_most_expensive_books(300))

    def test_equal_list_total_sum(self):
        self.assertEqual(round(sum([pair[1] for pair in Tome_Rater.get_n_most_expensive_books(3)])), 138)

class TestUserBookWorth(unittest.TestCase):
    def test_equal_user_worh(self):
        self.assertEqual(round(Tome_Rater.get_worth_of_user("alan@turing.com")[1]), 156)

if __name__ == '__main__':
    unittest.main()
