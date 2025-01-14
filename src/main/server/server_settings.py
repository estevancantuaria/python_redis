from flask import Flask

from src.models.sqlite.settings.connection import SqliteConnectionHandler
from src.models.redis.settings.connections import RedisConnectionHandler

redis_connection_handler = RedisConnectionHandler()
sqlite_connection_handler = SqliteConnectionHandler()

app = Flask(__name__)

from src.main.routes.products_routes import products_routes_bp

app.register_blueprint(products_routes_bp)

