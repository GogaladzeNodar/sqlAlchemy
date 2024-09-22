from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base  # Import Base from models.py


class DatabaseConfig:
    def __init__(self, db_name: str):
        """
        Initialize the DatabaseConfig object for an SQLite3 database
        :param db_name: The name of the SQLite3 database file
        """
        self.__db_name = db_name
        self.__db_url = self.__build_db_url()
        self.__engine = self.__create_engine()
        self.__SessionLocal = self.__create_session()
        # self.Base = declarative_base()

    def __build_db_url(self):
        """
        Private method to build the database URL
        :return: The SQLite database URL.
        """
        return f"sqlite:///{self.__db_name}.db"

    def __create_engine(self):
        """
        Private method to create the SQLAlchemy engine.
        :return: The SQLAlchemy engine connected to the database.
        """
        engine = create_engine(self.__db_url)
        print(f"SQLite3 engine created for database: {self.__db_name}.db")
        return engine

    def __create_session(self):
        """
        Private method to create a scoped session for database transactions.
        :return: A scoped session factory
        """
        session = scoped_session(sessionmaker(bind=self.__engine))
        print(f"Session configured for database: {self.__db_name}.db")
        return session

    def create_tables(self):
        """
        Public method to create all tables based on defined models.
        This method can be accesed outside the class.
        """
        Base.metadata.create_all(bind=self.__engine)
        print("All tables created")

    def get_session(self):
        """
        Public method to provide a new session for interacting with the database.
        This is the primary interface for external code to interact with the database session.
        :return: A new session from the session factory.
        """
        return self.__SessionLocal()

    def close_session(self):
        """
        Public method to close the current session.
        This method ensures that the session is properly closed after database operations.
        """
        self.__SessionLocal.remove()
        print("Database session closed")
