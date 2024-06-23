import logging

import boto3

from product_stock_check.check_products import check_all_products

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

sns = boto3.client("sns")


def lambda_handler(event, context):
    logging.info("Lambda function triggered.")
    check_all_products(sns_client=sns, logger=logger)
