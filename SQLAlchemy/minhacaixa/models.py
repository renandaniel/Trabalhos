from sqlalchemy import Column, DateTime, ForeignKey, Integer, Numeric, Sequence, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class Grupo(Base):
    __tablename__ = 'grupo'

    codigo = Column(Integer, Sequence('grupo_codigo_seq'), primary_key=True)
    nome = Column(String(50))
    razao_social = Column(String(50))
    cnpj = Column(String(20))


class Cliente(Base):
    __tablename__ = 'cliente'

    codigo = Column(Integer, Sequence('cliente_codigo_seq'), primary_key=True)
    nome = Column(String(50))
    rua = Column(String(50))
    cidade = Column(String(50))
    nascimento = Column(DateTime)


class Agencia(Base):
    __tablename__ = 'agencia'

    codigo = Column(Integer, Sequence('agencia_codigo_seq'), primary_key=True)
    nome = Column(String(50))
    cidade = Column(String(50))
    fundos = Column(Numeric(20, 2))
    grupo_codigo = Column(Integer, ForeignKey('grupo.codigo'))

    grupo = relationship('Grupo', backref='agencias')


class Conta(Base):
    __tablename__ = 'conta'

    agencia_codigo = Column(Integer, ForeignKey('agencia.codigo'))
    numero = Column(String(10), primary_key=True)
    cliente_codigo = Column(Integer, ForeignKey('cliente.codigo'))
    saldo = Column(Numeric(20, 2))
    abertura = Column(DateTime)

    agencia = relationship('Agencia', backref='contas')
    cliente = relationship('Cliente', backref='contas')


class Emprestimo(Base):
    __tablename__ = 'emprestimo'

    agencia_codigo = Column(Integer, ForeignKey('agencia.codigo'))
    cliente_codigo = Column(Integer, ForeignKey('cliente.codigo'))
    codigo = Column(String(10), primary_key=True)
    total = Column(Numeric(20, 2))

    agencia = relationship('Agencia', backref='emprestimos')
    cliente = relationship('Cliente', backref='emprestimos')


class Depositante(Base):
    __tablename__ = 'depositante'

    codigo = Column(Integer, Sequence('depositante_codigo_seq'), primary_key=True)
    agencia_codigo = Column(Integer, ForeignKey('agencia.codigo'))
    conta_numero = Column(String(10), ForeignKey('conta.numero'))
    cliente_codigo = Column(Integer, ForeignKey('cliente.codigo'))
    valor = Column(Numeric(20, 2))
    data = Column(DateTime)

    agencia = relationship('Agencia', backref='depositantes')
    conta = relationship('Conta', backref='depositantes')
    cliente = relationship('Cliente', backref='depositantes')
