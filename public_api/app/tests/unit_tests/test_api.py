import pytest
from httpx import AsyncClient


async def test_get_meme(ac: AsyncClient):
    response = await ac.get('public_api/memes')
    assert response.status_code == 200


async def test_get_meme_id(ac: AsyncClient):
    response = await ac.get('public_api/memes/1')
    assert response.status_code == 200


@pytest.mark.parametrize('title, description, status_code', [
    ('333', 'Картинка', 422),
    ('Картинка123', 'stg', 422),
    ('Картинка123', 'Адекватный размер сторок', 200),

])
async def test_add_meme(
        title,
        description,
        status_code,
        ac: AsyncClient
):
    file = open(r'C:\Users\slaav\PycharmProjects\mad_test\public_api\app\tests\unit_tests\11.jpg', 'rb')
    response = await ac.post(
        'api/login',
        json={
            'title': title,
            'description': description
        },
        files={'file': file}
    )

    assert response.status_code == status_code


@pytest.mark.parametrize('title, description, status_code', [
    ('333', 'Картинка', 422),
    ('Картинка123', 'stg', 422),
    ('Картинка123', 'Адекватный размер сторок', 200),

])
async def test_update_meme(
        title,
        description,
        status_code,
        ac: AsyncClient
):
    file = open(r'C:\Users\slaav\PycharmProjects\mad_test\public_api\app\tests\unit_tests\11.jpg', 'rb')
    response = await ac.put(
        'api/login',
        json={
            'title': title,
            'description': description
        },
        files={'file': file}
    )

    assert response.status_code == status_code


async def test_delete_meme(ac: AsyncClient):
    response = await ac.delete('public_api/memes/1')
    assert response.status_code == 200
