from product_stock_check.util import get_product_page_soup


def check_stock() -> bool:
    """Syd's linen Abercrombie pants that Finley tore a hole in."""
    soup = get_product_page_soup(
        product_url="https://www.abercrombie.com/shop/us/p/a-and-f-sloane-tailored-linen-blend-pant-55136826",
    )
    size_ele = soup.find(attrs={"id": "radio_size_primary_24"})
    is_available = size_ele.parent.attrs["data-state"] != "disabled"
    return is_available
