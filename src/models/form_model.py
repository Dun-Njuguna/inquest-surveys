from sqlalchemy import Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship
from .base import Base

class Form(Base):
    __tablename__ = "forms"  # Define the table name in the database

    # Define columns for the 'forms' table
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    form_data = Column(JSON, nullable=False)  # Store form data as JSON

    # Define relationships with other models
    survey = relationship("Survey", back_populates="forms")
    # 'survey' establishes a many-to-one relationship with the 'Survey' model
    # 'back_populates' allows for bidirectional access, linking the 'forms' attribute in the 'Survey' model
