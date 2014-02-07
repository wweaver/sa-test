from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, UnicodeText

from satest.model.base import Model


class Post(Model):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    subject = Column(UnicodeText, nullable=False)
    body = Column(UnicodeText, nullable=False)
