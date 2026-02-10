import boto3
from moto import mock_aws
from app.handlers.delete import handler
from app.config import AWS_REGION, DYNAMO_TABLE, S3_BUCKET

@mock_aws
def test_delete_image_success():
    s3 = boto3.client("s3", region_name=AWS_REGION)
    # s3.create_bucket(Bucket=S3_BUCKET)
    s3.create_bucket(
        Bucket=S3_BUCKET,
        CreateBucketConfiguration={"LocationConstraint": AWS_REGION}
    )
    s3.put_object(Bucket=S3_BUCKET, Key="img1", Body=b"data")

    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    table = dynamodb.create_table(
        TableName=DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    table.put_item(Item={"image_id": "img1", "user_id": "user1"})

    event = {"pathParameters": {"image_id": "img1"}}
    response = handler(event, None)

    assert response["statusCode"] == 200
    assert "deleted" in response["body"]


@mock_aws
def test_delete_image_not_found():
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    dynamodb.create_table(
        TableName=DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    event = {"pathParameters": {"image_id": "invalid"}}
    response = handler(event, None)

    assert response["statusCode"] == 404
