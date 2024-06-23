from typing import Any

import requests
from bs4 import BeautifulSoup


def send_notification(
    sns_client: Any,
    message: str,
    subject: str,
    topic_arn: str,
):
    return sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject,
    )


def get_product_page_soup(product_url, request_kwargs: dict = {}) -> BeautifulSoup:
    r = requests.get(product_url, **request_kwargs)
    soup = BeautifulSoup(r.content, "html.parser")
    return soup


def get_product_page_selenium(product_url):
    pass
