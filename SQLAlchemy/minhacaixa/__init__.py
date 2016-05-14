from sqlalchemy import create_engine
import os


engine = create_engine(os.environ.get('DATABASE_URL', 'sqlite:///:memory:'), echo=True)
