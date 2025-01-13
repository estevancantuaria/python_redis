from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.redis.repository.redis_repository import RedisRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, repository: ProductsRepository, redis_repo: RedisRepository) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = repository
        
    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        pass