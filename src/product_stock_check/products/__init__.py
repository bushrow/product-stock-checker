from product_stock_check.products.a_f_pants import (
    check_stock as check_abercrombie_pants,
)

ALL_PRODUCTS = {
    "a_f_pants": {
        "name": "A&F Linen Pants",
        "url": "https://www.abercrombie.com/shop/us/p/a-and-f-sloane-tailored-linen-blend-pant-55136826",
        "check_func": check_abercrombie_pants,
    }
    # "product_id": {
    #     "name": "Product Name"
    #     "url": "https://www.vendor.com/store/product.html"
    #     "check_func": product_function_name
    # }
}

__all__ = ["ALL_PRODUCTS"]
