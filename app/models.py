from dataclasses import dataclass
from typing import Dict
import uuid
import time

@dataclass
class ImageMetadata:
    image_id: str
    user_id: str
    filename: str
    content_type: str
    created_at: int
    tags: list

    @staticmethod
    def create(user_id, filename, content_type, tags):
        return ImageMetadata(
            image_id=str(uuid.uuid4()),
            user_id=user_id,
            filename=filename,
            content_type=content_type,
            created_at=int(time.time()),
            tags=tags
        )

    def to_item(self) -> Dict:
        return self.__dict__
