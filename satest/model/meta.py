from sqlalchemy.orm import sessionmaker, scoped_session

from satest.model.base import Model

__all__ = ['metadata', 'Session']

metadata = Model.metadata
Session = scoped_session(sessionmaker(autocommit=True, autoflush=True))
