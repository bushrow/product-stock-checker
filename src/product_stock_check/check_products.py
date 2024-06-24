import logging
import os
from typing import Any, Callable

import boto3

from product_stock_check.products import ALL_PRODUCTS
from product_stock_check.util import send_notification


def check_all_products(
    sns_topic_arn: str | None = None,
    sns_client: Any = None,
    logger: logging.Logger | None = None,
):
    """
    Iterate through `ALL_PRODUCTS` and check status of each product.

    Parameters
    ----------
    sns_topic_arn : str | None, optional
        SNS Topic ARN used for notifications. If None, it will attempt to pull the `SNS_TOPIC_ARN` environment variable. By default None
    sns_client : Any, optional
        Boto3 client for SNS, by default None. If None, a new client will be instantiated with default profile.
    logger : logging.Logger | None, optional
        Logger
    """
    sns_topic_arn = sns_topic_arn or os.environ["SNS_TOPIC_ARN"]
    sns_client = sns_client or boto3.client("sns")
    logger = logger or logging.getLogger(__name__)
    logger.info(
        f"Checking all configured products' stock ({len(ALL_PRODUCTS)} products configured)."
    )
    for _, product_dict in ALL_PRODUCTS.items():
        check_product_available(
            product_name=product_dict["name"],
            product_url=product_dict["url"],
            product_check_func=product_dict["check_func"],
            sns_topic_arn=sns_topic_arn,
            sns_client=sns_client,
            logger=logger,
        )


def check_product_available(
    product_name: str,
    product_url: str,
    product_check_func: Callable,
    sns_topic_arn: str,
    sns_client: Any,
    logger: logging.Logger,
) -> None:
    """
    Check if a product is in-stock using the provided check function.

    Parameters
    ----------
    product_name : str
        Name of the product to be used in notification and logging
    product_url : str
        URL to provide to the product stock check function
    product_check_func : Callable
        Function that returns boolean representing whether the item is in stock
    sns_topic_arn : str
        ARN of the SNS Topic to publish notifications to on re-stock.
    sns_client : Any
        Boto3 client for SNS
    logger : logging.Logger
        Logger
    """
    logger.info(f"Checking availability for {product_name}...")
    available = product_check_func()
    if available:
        logger.info(f"{product_name} is available. Notification sent via SNS.")
        send_notification(
            sns_client=sns_client,
            message=f"Get {product_name} now, while it's available:\n{product_url}",
            subject=f"{product_name} is Now Available!",
            topic_arn=sns_topic_arn,
        )
    else:
        logger.info(f"{product_name} not available at this time.")
