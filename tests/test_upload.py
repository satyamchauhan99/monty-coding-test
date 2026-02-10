import json
import boto3
from moto import mock_aws
from app.handlers.upload import handler
from app.config import AWS_REGION, DYNAMO_TABLE, S3_BUCKET

@mock_aws
def test_upload_image():
    # ---- Setup S3 ----
    s3 = boto3.client("s3", region_name=AWS_REGION)
    # s3.create_bucket(Bucket=S3_BUCKET)
    s3.create_bucket(
        Bucket=S3_BUCKET,
        CreateBucketConfiguration={"LocationConstraint": AWS_REGION}
    )


    # ---- Setup DynamoDB ----
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)
    dynamodb.create_table(
        TableName=DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    event = {
        "body": json.dumps({
            "user_id": "user1",
            "filename": "img.jpg",
            "content_type": "image/jpeg",
            "image": "aGVsbG8=",  # base64("hello")
            "tags": ["test"]
        })
    }

    response = handler(event, None)
    assert response["statusCode"] == 201
