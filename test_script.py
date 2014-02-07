from sqlalchemy import create_engine

from satest.model import init_model, import_models
from satest.model import meta

engine = create_engine('postgresql://testing@localhost:5432/testing')

init_model(engine)
m = import_models('Post')

meta.metadata.drop_all(engine)
meta.metadata.create_all(engine)
