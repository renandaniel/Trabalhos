from . import engine, Session
from .models import Base, Grupo


Base.metadata.create_all(engine)

db = Session()
db.add_all([
    Grupo(nome='MyBank',
          razao_social='MyBank International SA',
          cnpj='11.222.333/0001-44'),
])
db.commit()
