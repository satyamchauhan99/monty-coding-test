from app.services.image_service import get_image_url
from app.services.dynamo_service import get_image
from app.utils.response import success, error

def handler(event, context):
    image_id = event["pathParameters"]["image_id"]
    image = get_image(image_id)

    if not image:
        return error("Image not found", 404)

    url = get_image_url(image_id)
    return success({"url": url})
