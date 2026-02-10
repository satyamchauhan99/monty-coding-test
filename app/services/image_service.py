from app.aws_clients import get_s3_client
from app.config import S3_BUCKET

def upload_to_s3(image_bytes, key, content_type):
    get_s3_client().put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=image_bytes,
        ContentType=content_type
    )

def get_image_url(key):
    return get_s3_client().generate_presigned_url(
        "get_object",
        Params={"Bucket": S3_BUCKET, "Key": key},
        ExpiresIn=3600
    )

def delete_from_s3(key):
    get_s3_client().delete_object(Bucket=S3_BUCKET, Key=key)
