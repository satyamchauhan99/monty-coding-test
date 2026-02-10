from app.services.dynamo_service import list_images
from app.utils.response import success

def handler(event, context):
    params = event.get("queryStringParameters") or {}
    images = list_images(filters=params)
    return success(images)
