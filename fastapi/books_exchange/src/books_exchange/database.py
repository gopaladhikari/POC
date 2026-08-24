from sqlmodel import create_engine, Session, SQLModel

db_url = "sqlite:///books_exchange.db"

engine = create_engine(db_url, echo=True)


def create_table():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
