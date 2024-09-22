from database_conf import DatabaseConfig
from fake_data import FakeAuthorGenerator, FakeBookGenerator
from db_queries import QueryManager
from models import Author, Book


def main():
    # Initialize database configuration
    db_config = DatabaseConfig("mydatabase")
    db_config.create_tables()

    # Open a session after creating tables
    session = db_config.get_session()  # Open a session

    # Generate fake data
    author_generator = FakeAuthorGenerator()
    authors = author_generator.generate_fake_authors(500)  # Generate 500 authors

    book_generator = FakeBookGenerator(authors)
    books = book_generator.generate_fake_books(
        1000
    )  # Generated 1000 books. No trees were harmed ;)

    # Insert generated fake data into the database
    session.add_all(authors)
    session.add_all(books)
    session.commit()  # Commit the changes to the database

    # Run database queries
    query_manager = QueryManager(session)
    print("\n")
    print(
        "*******************************************************************************************************************"
    )

    # Example queries
    book_with_most_pages = query_manager.find_book_with_most_pages()
    print(f"Book with the most pages: {book_with_most_pages}\n")
    print("Database now knows which book has the most pages. Bigger is better?")
    print(
        "*******************************************************************************************************************"
    )

    avg_pages = query_manager.find_average_pages_in_books()
    print(f"Average number of pages: {avg_pages}\n")
    print(
        "*******************************************************************************************************************"
    )

    youngest_author = query_manager.find_youngest_author()
    print(f"Youngest author: {youngest_author}\n")
    print(
        "*******************************************************************************************************************"
    )

    authors_with_no_books = query_manager.find_authors_with_no_books()
    print(
        f"These authors have written exactly zero books. Hey, everyone's gotta start somewhere... or not: {authors_with_no_books}\n"
    )
    print(
        "*******************************************************************************************************************"
    )

    authors_with_more_than_three_books = (
        query_manager.find_authors_with_more_than_three_books()
    )
    print(f"Authors with more than 3 books: {authors_with_more_than_three_books}\n")
    print(
        "*******************************************************************************************************************"
    )

    # Close the session when done
    session.close()


if __name__ == "__main__":
    main()
