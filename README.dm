# SQLAlchemy Project

This project demonstrates the use of **SQLAlchemy**, an ORM (Object Relational Mapper) for Python, to interact with an SQLite database. The project includes data modeling, fake data generation, and running various queries on the database.

## Project Structure

- `main.py`: The main entry point of the application. It initializes the database, generates fake data, and runs various database queries.
- `database_conf.py`: Contains the configuration for the database, including session handling and table creation.
- `models.py`: Defines the SQLAlchemy models for the **Author** and **Book** entities.
- `fake_data.py`: Generates fake authors and books using the **Faker** library.
- `db_queries.py`: Contains methods to run different queries on the database.
- `venv/`: The virtual environment (ignored by Git).
  
## Requirements

- Python 3.12.3
- **SQLAlchemy** for ORM
- **Faker** for generating fake data

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/GogaladzeNodar/sqlAlchemy.git
    cd sqlAlchemy
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the application**:

    ```bash
    python main.py
    ```

2. The app will:
    - Create an SQLite database named `mydatabase.db`.
    - Generate 500 fake authors and 1000 fake books.
    - Insert the generated data into the database.
    - Run various queries such as:
        - Finding the book with the most pages.
        - Calculating the average number of pages in books.
        - Finding the youngest author.
        - Listing authors with no books.
        - Finding authors who have written more than three books.

## Models

### Author
- `id`: Integer (Primary Key)
- `first_name`: String (Not null)
- `last_name`: String (Not null)
- `birth_date`: Date
- `birth_place`: String
- Relationship with **Book** (Many-to-Many)

### Book
- `id`: Integer (Primary Key)
- `book_name`: String (Not null)
- `category_name`: String
- `page_quantity`: Integer
- `publish_date`: Date
- Relationship with **Author** (Many-to-Many)

## Queries

Here are some of the queries you can run using the `QueryManager`:

- Find the book with the most pages.
- Get the average number of pages in books.
- Find the youngest author.
- List authors with no books.
- List authors with more than three books.


