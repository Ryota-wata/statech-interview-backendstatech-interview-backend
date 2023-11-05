from sqlalchemy import Column, Integer, ForeignKey
from api.db import Base

class UserAnswer(Base):
    __tablename__ = "user_answers"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    question_id = Column(Integer, ForeignKey("questions.id"))
    choice_id = Column(Integer, ForeignKey("choices.id"))
    took_exam_num = Column(Integer)

