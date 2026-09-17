from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy registers their tables.
from app.models.task import Task  # noqa: E402, F401
from app.models.user import User  # noqa: E402, F401
