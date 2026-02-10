import boto3
from moto import mock_aws
from app.handlers.list_images import handler
from app.config import AWS_REGION, DYNAMO_TABLE

@mock_aws
def test_list_images_with_filters():
    dynamodb = boto3.resource("dynamodb", region_name=AWS_REGION)

    table = dynamodb.create_table(
        TableName=DYNAMO_TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST"
    )

    table.put_item(Item={
        "image_id": "img1",
        "user_id": "user1",
        "tags": ["nature"]
    })

    table.put_item(Item={
        "image_id": "img2",
        "user_id": "user2",
        "tags": ["food"]
    })

    event = {
        "queryStringParameters": {
            "user_id": "user1",
            "tag": "nature"
        }
    }

    response = handler(event, None)

    assert response["statusCode"] == 200
    assert "img1" in response["body"]
    assert "img2" not in response["body"]
