from sqlalchemy import (
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    Table,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# Association Table for Many-to-Many relationship between Author and Book
author_book_association = Table(
    "author_book",
    Base.metadata,
    Column("author_id", Integer, ForeignKey("author.id")),
    Column("book_id", Integer, ForeignKey("book.id")),
    UniqueConstraint("author_id", "book_id", name="uix_author_book"),
    # Books and authors officially in a relationship. It’s complicated."
)


class Author(Base):
    """
    Initialize Author Table
    Fields: id, first_name, last_name, birth_date, birth_place
    """

    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date)
    birth_place = Column(String)

    # Relationship to Book (Many-to-Many)
    books = relationship(
        "Book", secondary=author_book_association, back_populates="authors"
    )

    def __init__(self, first_name, last_name, birth_date, birth_place):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.birth_place = birth_place

    def __repr__(self):
        return f"Author(name={self.first_name} {self.last_name}, birth_date={self.birth_date}, birth_place={self.birth_place})"


class Book(Base):
    """
    Initialize Book table
    Fields: id, book_name, category_name, page_quantity, publish_date
    """

    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)
    category_name = Column(String)
    page_quantity = Column(Integer)
    publish_date = Column(Date)

    # Relationship to Author (Many-to-Many)
    authors = relationship(
        "Author", secondary=author_book_association, back_populates="books"
    )

    def __init__(self, book_name, category_name, page_quantity, publish_date):
        self.book_name = book_name
        self.category_name = category_name
        self.page_quantity = page_quantity
        self.publish_date = publish_date

    def __repr__(self):
        return f"Book(name={self.book_name}, category={self.category_name}, publish_date={self.publish_date})"
