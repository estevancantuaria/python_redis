from flask import Flask
import sqlite3

from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.models.redis.settings.connections import RedisConnectionHandler

redis_connection_handler = RedisConnectionHandler()

class SqliteConnectionHandler:
    def __init__(self):
        self.__connection = None

    def get_connection(self):
        if self.__connection is None:
            try:
                self.__connection = sqlite3.connect('storage.db')
                # Opcional: configurar para retornar rows como dicionários
                self.__connection.row_factory = sqlite3.Row
            except sqlite3.Error as error:
                print(f"Erro ao conectar ao SQLite: {error}")
                raise
        return self.__connection

sqlite_connection_handler = SqliteConnectionHandler()

app = Flask(__name__)

from src.main.routes.products_routes import products_routes_bp

app.register_blueprint(products_routes_bp)

