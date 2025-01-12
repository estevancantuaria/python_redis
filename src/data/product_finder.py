from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.redis.repository.redis_repository import RedisRepository
class ProductFinder:
    def __init__(self, repository: ProductsRepository, redis_repo: RedisRepository) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = repository
        
        