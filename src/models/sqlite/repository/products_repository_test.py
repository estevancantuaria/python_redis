import pytest

from src.models.sqlite.settings.connection import SqliteConnectionHandler
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandler()
conn = conn_handle.connect()

@pytest.mark.skip(reason="interacao com o banco de dados")
def test_insert_product():
    repo = ProductsRepository(conn)
    
    name = "Product 1"
    price = 10.0
    quantity = 10

    repo.insert_product(name, price, quantity)

def test_find_product_by_name():
    repo = ProductsRepository(conn)
    name = "Product 1"
    response = repo.find_product_by_name(name)
    print(response)