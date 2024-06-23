import datetime
import logging
from typing import Any, Callable

import boto3

from product_stock_check.products import ALL_PRODUCTS
from product_stock_check.util import send_notification


def check_all_products(sns_client: Any = None, logger: logging.Logger | None = None):
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
            sns_client=sns_client,
            logger=logger,
        )


def check_product_available(
    product_name: str,
    product_url: str,
    product_check_func: Callable,
    sns_client: Any,
    logger: logging.Logger,
) -> bool:
    start_time: str = (datetime.datetime.now(datetime.timezone.utc)).strftime(
        "%Y-%m-%d %I:%M %p %Z"
    )
    logger.info(f"[{start_time}] Checking availability for {product_name}...")
    available = product_check_func()
    check_time: str = (datetime.datetime.now(datetime.timezone.utc)).strftime(
        "%Y-%m-%d %I:%M %p %Z"
    )
    if available:
        logger.info(
            f"[{check_time}] {product_name} is available. Notification sent via SNS."
        )
        send_notification(
            sns_client=sns_client,
            message=f"Get {product_name} now, while it's available:\n{product_url}",
            subject=f"{product_name} is Now Available!",
        )
    else:
        logger.info(f"[{check_time}] {product_name} not available at this time.")
