from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.redis.repository.redis_repository import RedisRepository
from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class ProductFinder:
    def __init__(self, repository: ProductsRepository, redis_repo: RedisRepository) -> None:
        self.__redis_repo = redis_repo
        self.__products_repo = repository
        
    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        product_name = http_request.params["product_name"]
        product = None
        product = self.__find_in_cache(product_name)

        if not product:
            product = self.__find_in_sql(product_name)
            self.__insert_in_cache(product)
        
        return self.__format_response(product)
        
    def __find_in_cache(self, product_name: str) -> tuple:
        product_infos = self.__redis_repo.get_key(product_name)
        if product_infos:
            product_infos_list = product_infos.split(",")
            return (0,product_name, product_infos_list[0], product_infos_list[1])
        
        return None

    def __find_in_sql(self, product_name: str) -> tuple:
        product = self.__products_repo.find_product_by_name(product_name)
        if not product:
            raise Exception("Product not found")
        
        return product
    
    def __insert_in_cache(self, product: tuple) -> None:
        product_name = product[1]
        value = f"{product[2]},{product[3]}"
        self.__redis_repo.insert_ex(product_name, value, ex=60)
    
    def __format_response(self, product: tuple) -> HttpResponse:
        return HttpResponse(
            status_code=200,
            body={
                "product_name": product[1],
                "price": product[2],
                "description": product[3]
            }
        )
