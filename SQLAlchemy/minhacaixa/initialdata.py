from datetime import datetime

from . import engine, Session
from .models import Base, Grupo, Cliente


Base.metadata.create_all(engine)

db = Session()
db.add_all([
    Grupo(nome='MyBank',
          razao_social='MyBank International SA',
          cnpj='11.222.333/0001-44'),

    Cliente(nome='Ana',
            rua='XV de Novembro',
            cidade='Joinville',
            nascimento=datetime(1980, 8, 6)),
    Cliente(nome='Laura',
            rua='07 de Setembro',
            cidade='Blumenau',
            nascimento=datetime(1981, 8, 8)),
    Cliente(nome='Vânia',
            rua='01 de Maio',
            cidade='Blumenau',
            nascimento=datetime(1982, 8, 6)),
    Cliente(nome='Franco',
            rua='Felipe Schmidt',
            cidade='Florianopolis',
            nascimento=datetime(1985, 8, 6)),
    Cliente(nome='Eduardo',
            rua='Beria Mar Norte',
            cidade='Florianópolis',
            nascimento=datetime(1970, 11, 10)),
    Cliente(nome='Bruno',
            rua='24 de maio',
            cidade='Criciúma',
            nascimento=datetime(1982, 7, 5)),
    Cliente(nome='Rodrigo',
            rua='06 de agosto',
            cidade='Joinville',
            nascimento=datetime(1981, 8, 6)),
    Cliente(nome='Ricardo',
            rua='João Colin',
            cidade='Joinville',
            nascimento=datetime(1980, 2, 15)),
    Cliente(nome='Alexandre',
            rua='Margem esquerda',
            cidade='Blumenau',
            nascimento=datetime(1980, 3, 7)),
    Cliente(nome='Luciana',
            rua='Estreito',
            cidade='Florianópolis',
            nascimento=datetime(1987, 9, 6)),
    Cliente(nome='Juliana',
            rua='Iririu',
            cidade='Joinville',
            nascimento=datetime(1970, 1, 6)),
    Cliente(nome='Pedro',
            rua='Aventureiro',
            cidade='Joinville',
            nascimento=datetime(1975, 6, 8)),
    Cliente(nome='Julia',
            rua='Nova Brasília',
            cidade='Joinville',
            nascimento=datetime(1985, 3, 18)),
])
db.commit()
