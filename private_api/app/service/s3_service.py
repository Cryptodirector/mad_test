import os
from contextlib import asynccontextmanager

from aiobotocore.session import get_session

SECRET_KEY = os.getenv('SECRET_KEY')
ACCESS_KEY = os.getenv('ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')
ENDPOINT_URL = os.getenv('ENDPOINT_URL')


class S3Client:

    def __init__(self):
        self.config = {
            'aws_secret_key_id': SECRET_KEY,
            'aws_access_key_id': ACCESS_KEY,
            'endpoint_url': ENDPOINT_URL
        }
        self.bucket_name = BUCKET_NAME
        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client(
                's3',
                **self.config
        ) as s3_client:
            yield s3_client

    async def upload_file(
            self,
            file_path: str,
            file_name: str
    ):
        async with self.get_client() as client:
            with open(file_path, 'rb') as file:
                await client.put_object(
                    Bucket=self.bucket_name,
                    Key=file_name,
                    Body=file
                )
