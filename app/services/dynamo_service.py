from app.aws_clients import get_dynamodb_resource
from app.config import DYNAMO_TABLE

def get_table():
    dynamodb = get_dynamodb_resource()
    return dynamodb.Table(DYNAMO_TABLE)

def save_metadata(item):
    get_table().put_item(Item=item)

def list_images(filters=None):
    table = get_table()
    items = table.scan().get("Items", [])

    if filters:
        if "user_id" in filters:
            items = [i for i in items if i["user_id"] == filters["user_id"]]
        if "tag" in filters:
            items = [i for i in items if filters["tag"] in i.get("tags", [])]

    return items

def get_image(image_id):
    return get_table().get_item(Key={"image_id": image_id}).get("Item")

def delete_image(image_id):
    get_table().delete_item(Key={"image_id": image_id})
