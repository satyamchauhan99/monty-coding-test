from app.services.image_service import delete_from_s3
from app.services.dynamo_service import delete_image, get_image
from app.utils.response import success, error

def handler(event, context):
    image_id = event["pathParameters"]["image_id"]
    image = get_image(image_id)

    if not image:
        return error("Image not found", 404)

    delete_from_s3(image_id)
    delete_image(image_id)

    return success({"message": "Image deleted"})
