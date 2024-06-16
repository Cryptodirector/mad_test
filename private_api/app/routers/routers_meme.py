from fastapi import APIRouter, UploadFile
from private_api.app.service.s3_service import S3Client

router = APIRouter()


@router.post('/memes')
async def add_meme(file: UploadFile):
    await S3Client.upload_file(
        file_path=file,
        file_name=file.filename
    )


