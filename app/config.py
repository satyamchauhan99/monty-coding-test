import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION", "ap-south-1")
S3_BUCKET = os.getenv("S3_BUCKET_NAME", "instagram-images-demo")
DYNAMO_TABLE = os.getenv("DYNAMODB_TABLE_NAME", "ImageMetadata")
