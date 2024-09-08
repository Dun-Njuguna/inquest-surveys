from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class Survey(Base):
    __tablename__ = "surveys"

    title = Column(String, nullable=False)  # Title of the survey
    description = Column(Text, nullable=True)  # Detailed description of the survey
    is_active = Column(Boolean, default=True)  # Status of the survey

    # Relationships
    forms = relationship("Form", back_populates="survey")  # Related forms for the survey
    responses = relationship("Response", back_populates="survey")  # Responses associated with the survey
    user_surveys = relationship("UserSurvey", back_populates="survey")  # User interactions with the survey
