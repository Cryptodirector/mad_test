from fastapi import APIRouter, UploadFile, Query
from public_api.app.service.mem_service import Service
from sqlalchemy.exc import IntegrityError
from public_api.app.exceptions.meme_exceptions import WrongFormat, MemReady


router = APIRouter(
    prefix='/public_api',
    tags=['Публичный API']
)


# Получаем все мемы

@router.get('/memes')
async def get_memes():
    return await Service.get_meme()

# Получаем мемы по его id


@router.get('/memes/{id}')
async def get_meme_id(id: int):
    return await Service.get_meme_by_id(id)

# Создаем мем


@router.post('/memes')
async def add_meme_url(
        file: UploadFile,
        title: str = Query(max_length=50),
        description: str = Query(max_length=1000)

):
    if file.filename.split('.')[1] not in ['png', 'jpg', 'jpeg']:
        raise WrongFormat

    try:
        url = await Service.save_file(file)
        return await Service.add_meme(
            url,
            title,
            description
        )

    except IntegrityError:
        raise MemReady


# Обновляем мем

@router.put('/memes/{id}')
async def update_memes(
        id: int,
        file: UploadFile,
        title: str = Query(max_length=50),
        description: str = Query(max_length=1000)
):
    if file.filename.split('.')[1] not in ['png', 'jpg', 'jpeg']:
        raise WrongFormat

    try:
        url = await Service.save_file(file)
        return await Service.update_meme(
            url,
            title,
            description,
            id
        )

    except IntegrityError:
        raise MemReady


# Удаляем мем

@router.delete('/memes/{id}')
async def delete_memes(id: int):
    return await Service.delete_meme(id)