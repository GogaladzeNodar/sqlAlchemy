from sqlalchemy.orm import Session
from models import Author, Book
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


class QueryManager:
    def __init__(self, session: Session):
        """
        Initialize the query manager with a given SQLAlchemy session
        :param session: SQLAlchemy session object used for database interactions.
        """
        self.session = session

    def find_book_with_most_pages(self):
        """
        Finds and prints all fields of the book with the most pages.
        :return: The book with the most pages or None if an error occurs.
        """
        try:
            book = self.session.query(Book).order_by(Book.page_quantity.desc()).first()
            return book
        except SQLAlchemyError as e:
            print(f"Error finding the book with the most pages: {e}")
            return None

    def find_average_pages_in_books(self):
        """
        Finds and prints the average number of pages in all books.
        :return: The average number of pages or None if an error occurs.
        """
        try:
            avg_pages = self.session.query(func.avg(Book.page_quantity)).scalar()
            return avg_pages
        except SQLAlchemyError as e:
            print(f"Error finding the average number of pages: {e}")
            return None

    def find_youngest_author(self):
        """
        Finds and prints the youngest author.
        :return: The youngest Author instance or None if an error occurs.
        """
        try:
            youngest_author = (
                self.session.query(Author).order_by(Author.birth_date.desc()).first()
            )
            return youngest_author
        except SQLAlchemyError as e:
            print(f"Error finding the youngest author: {e}")
            return None

    def find_authors_with_no_books(self):
        """
        Finds and prints authors who have no books associated with them.
        :return: A list of Author instances or an empty list if an error occurs.
        """
        try:
            authors_without_books = (
                self.session.query(Author).filter(~Author.books.any()).all()
            )
            return authors_without_books
        except SQLAlchemyError as e:
            print(f"Error finding authors with no books: {e}")
            return []

    def find_authors_with_more_than_three_books(self):
        """
        Finds and prints 5 authors who have more than 3 books associated with them.
        :return: A list of Author instances or an empty list if an error occurs.
        """
        try:
            authors = (
                self.session.query(Author)
                .join(Author.books)
                .group_by(Author.id)
                .having(func.count(Book.id) > 3)
                .limit(5)
                .all()
            )
            return authors
        except SQLAlchemyError as e:
            print(f"Error finding authors with more than three books: {e}")
            return []
