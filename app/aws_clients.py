import boto3
from app.config import AWS_REGION

def get_s3_client():
    return boto3.client("s3", region_name=AWS_REGION)

def get_dynamodb_resource():
    return boto3.resource("dynamodb", region_name=AWS_REGION)


def get_dynamodb_table(table_name):
    return get_dynamodb_resource().Table(table_name)