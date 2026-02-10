import base64
import json
from app.models import ImageMetadata
from app.services.image_service import upload_to_s3
from app.services.dynamo_service import save_metadata
from app.utils.response import success, error

def handler(event, context):
    body = json.loads(event["body"])

    image_bytes = base64.b64decode(body["image"])
    metadata = ImageMetadata.create(
        user_id=body["user_id"],
        filename=body["filename"],
        content_type=body["content_type"],
        tags=body.get("tags", [])
    )

    upload_to_s3(image_bytes, metadata.image_id, metadata.content_type)
    save_metadata(metadata.to_item())

    return success({"image_id": metadata.image_id}, 201)
