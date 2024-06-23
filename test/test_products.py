from product_stock_check.products import ALL_PRODUCTS


def test_products() -> None:
    for _, prod_dict in ALL_PRODUCTS.items():
        assert isinstance(prod_dict["name"], str)
        assert isinstance(prod_dict["url"], str)
        assert callable(prod_dict["check_func"])
