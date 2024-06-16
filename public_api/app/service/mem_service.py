import shutil

from sqlalchemy import insert, select, delete, update
from public_api.app.models.meme_models import Images
from public_api.app.db.config import async_session_maker
from public_api.app.exceptions.meme_exceptions import IsNotFound


class Service:
    @staticmethod
    async def add_meme(
            url: str,
            title,
            description
    ) -> dict:
        async with async_session_maker() as session:

            await session.execute(
                insert(Images).values(
                    title=title,
                    description=description,
                    url_image=url,

                )
            )
            await session.commit()
            return {
                'status_code': 200,
                'detail': 'Мем создан!'
            }

    @staticmethod
    async def get_meme() -> dict:
        async with async_session_maker() as session:
            query = await session.execute(
                select(Images)
            )
            return query.scalars().all()

    @staticmethod
    async def get_meme_by_id(id: int) -> dict:
        async with async_session_maker() as session:
            query = await session.execute(
                select(Images).where(Images.id == id)
            )
            return query.scalars().all()

    @staticmethod
    async def update_meme(
        url,
        title,
        description,
        id,
    ) -> dict:

        async with async_session_maker() as session:

            await session.execute(
                update(Images).where(Images.id == id).values(
                    url_image=url,
                    title=title,
                    description=description,
                )
            )
            await session.commit()
            return {
                'status_code': 200,
                'detail': 'Мем обновлен!'
            }

    @staticmethod
    async def delete_meme(id: int) -> dict:
        async with async_session_maker() as session:
            result = await session.execute(
                delete(Images).where(Images.id == id)
            )
            if result:
                await session.commit()
                return {
                    'status_code': 200,
                    'detail': 'Мем обновлен!'
                }
            else:
                raise IsNotFound

    @staticmethod
    async def save_file(file) -> str:
        path = fr'C:\Users\slaav\PycharmProjects\mad_test\public_api\app\image\{file.filename}'
        with open(path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return path
