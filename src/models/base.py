from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, DateTime, func
from sqlalchemy.orm import Mapped

@as_declarative()
class Base:
    id: Mapped[int] = Column(Integer, primary_key=True, index=True)
    created_at: Mapped[DateTime] = Column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = Column(DateTime(timezone=True), onupdate=func.now())

    @declared_attr
    def __tablename__(cls) -> str:
        """Dynamically set the table name based on the class name."""
        return cls.__name__.lower()
