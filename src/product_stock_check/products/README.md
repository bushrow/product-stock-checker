## Implement New Product Checks Here

To add new products, create a new `.py` file in this directory that contains the logic for determining whether or not that product is in stock. Leverage shared functions from `product_stock_check.util`.  

Create a function that returns a boolean of whether the product is in stock; import that function to this directory's `__init__.py` file and create a new entry in `ALL_PRODUCTS` in the provided format.