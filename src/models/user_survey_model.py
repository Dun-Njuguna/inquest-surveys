from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from .base import Base

class UserSurvey(Base):
    __tablename__ = "user_surveys"

    user_id = Column(Integer, primary_key=True)  # Foreign key to the User model
    survey_id = Column(Integer, ForeignKey("surveys.id"), primary_key=True)  # Foreign key to the Survey model

    # Relationships
    survey = relationship("Survey", back_populates="user_surveys")  # Back reference to the Survey model
    responses = relationship("Response", back_populates="user_survey")  # Back reference to the Response model
