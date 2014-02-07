from sqlalchemy.ext.declarative import declarative_base

__all__ = ['Model']


class BaseModel(object):

    def __repr__(self):
        return '{0.__class__.__name__(id={0}.id)'.format(self)

Model = declarative_base(cls=BaseModel)
