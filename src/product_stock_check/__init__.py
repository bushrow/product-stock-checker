import logging

from product_stock_check.check_products import (
    check_all_products,
    check_product_available,
)
from product_stock_check.lambda_function import lambda_handler

logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] (%(asctime)s) - %(name)s - %(message)s"
)

__all__ = ["check_all_products", "check_product_available", "lambda_handler"]
