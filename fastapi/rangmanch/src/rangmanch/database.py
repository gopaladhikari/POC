from sqlmodel import SQLModel, Session, create_engine

database_url = "sqlite:///rangmanch.db"


engine = create_engine(database_url, echo=True)


def create_tables():
    """Create tables in the database."""

    SQLModel.metadata.create_all(engine)


def get_session():
    """Dependency that provides a database session for request."""
    with Session(engine) as session:
        yield session
