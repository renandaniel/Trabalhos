.. figure:: http://www.sqlalchemy.org/img/sqla_logo.png
  :alt: SQLAlchemy
  :width: 150px


Minha Caixa - SQLAlchemy
========================

Banco de dados Minha Caixa no ORM `SQLAlchemy <http://www.sqlalchemy.org/>`_.


Arquivos
--------

`esquema.rst <esquema.rst>`_
  Esquema do banco de dados.

`minhacaixa/models.py <minhacaixa/models.py>`_
  Models do ORM (Tabelas).

`minhacaixa/initialdata.py <minhacaixa/initialdata.py>`_
  Dados iniciais do banco de dados.


Estilo de Código
----------------

Utilizar o `flake8 <https://flake8.readthedocs.io/>`_ conforme configurado no `setup.cfg <setup.cfg>`_.


Comandos
--------

Criar Estrutura
~~~~~~~~~~~~~~~

.. code-block:: sh

  pip install -r requirements.txt  # Instala as dependências
  pip install mysqlclient  # Para suporte ao MySQL
  pip install psycopg2  # Para suporte ao PostgreSQL

  # Criar estrutura
  DATABASE_URL='postgres://usuario:senha@host:porta/nome_db' python -m minhacaixa.initialdata


Consulta
~~~~~~~~

.. code-block:: python

  from minhacaixa import Session
  from minhacaixa.models import Grupo

  db = Session()

  db.query(Grupo).all()
