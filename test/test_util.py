from botocore.stub import Stubber

from product_stock_check.util import (
    send_notification,
    get_product_page_soup,
    get_product_page_selenium,
)


def test_send_notification() -> None:
    # with Stubber() as stubber:
    #     stubber.add_response("")
    #     send_notification(
    #         sns_client=stubber,
    #         message="testing",
    #         subject="testing",
    #         topic_arn="arn:aws:::",
    #     )
    pass


def test_get_product_page_soup() -> None:
    pass


def test_get_product_page_selenium() -> None:
    pass
