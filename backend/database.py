from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData
from sqlalchemy.inspection import inspect

class DatabaseSQLAlchemy:
    _db = None

    @staticmethod
    def get_db():
        if not DatabaseSQLAlchemy._db:
            DatabaseSQLAlchemy._db = SQLAlchemy(model_class=Base)
        return DatabaseSQLAlchemy._db

    @staticmethod
    def init_app(app):
        if not DatabaseSQLAlchemy._db:
            DatabaseSQLAlchemy._db = SQLAlchemy(model_class=Base)
        DatabaseSQLAlchemy._db.init_app(app)

    @staticmethod
    def reset_db():
        db = DatabaseSQLAlchemy.get_db()
        with db.engine.connect() as conn:
            conn.execute("DROP SCHEMA IF EXISTS public CASCADE;")
            conn.execute("CREATE SCHEMA public;")
            db.session.commit()


