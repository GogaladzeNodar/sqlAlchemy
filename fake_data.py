from faker import Faker
from models import Author, Book
import random
from datetime import timedelta, date

# Fake data generator
fake = Faker()
categories = [
    "Fiction",
    "Non-fiction",
    "Science Fiction",
    "Fantasy",
    "Biography",
    "History",
]


class FakeAuthorGenerator:
    def __init__(self):
        """
        Initialize the fake author generator class.
        Uses Faker to generate fake names and places
        """

        self.authors = []

    def generate_fake_author(self):
        """
        Generate a single fake Author instance.
        :return: An instance of the Author class
        """

        first_name = fake.first_name()
        last_name = fake.last_name()
        birth_date = fake.date_of_birth(minimum_age=20, maximum_age=100)
        birth_place = fake.city()

        return Author(
            first_name=first_name,
            last_name=last_name,
            birth_date=birth_date,
            birth_place=birth_place,  # Authors now have birthplaces. Geographical accuracy not guaranteed.
        )

    def generate_fake_authors(self, n):
        """
        Generate a list of n fake Author instances
        :param: The number of authors to generate
        :return: List of Author instances.
        """

        self.authors = [self.generate_fake_author() for _ in range(n)]
        return self.authors


class FakeBookGenerator:
    def __init__(self, authors):
        """
        Initialize the fake book generator class.
        Requires a list of authors to associate books with.
        :param authors: List of Author instances.
        """
        self.authors = authors
        self.books = []

    def generate_fake_book(self):
        """
        Generates a single fake Book instance and randomly associates it with an author.
        :return: An instance of the Book class.
        """

        book_name = fake.sentence(nb_words=3).rstrip(".")
        category_name = random.choice(categories)
        page_quantity = random.randint(20, 1000)
        publish_date = fake.date_between(start_date="-100y", end_date="today")

        # Create a new Book instance
        book = Book(
            book_name=book_name,
            category_name=category_name,
            page_quantity=page_quantity,
            publish_date=publish_date,
        )

        # Randomly assign authors to the book (many-to-Many relationship) We don't care who owns whose book
        num_authors = random.randint(1, 3)
        book.authors = random.sample(self.authors, num_authors)

        return book

    def generate_fake_books(self, n):
        """
        Generates a list of n fake Book instance.
        :param n: The number of books to generate.
        :return: A list of Book instances.
        """
        self.books = [self.generate_fake_book() for _ in range(n)]
        return self.books
