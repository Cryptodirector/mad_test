from fastapi import HTTPException, status


class BException(HTTPException):
    status_code = None
    detail = None

    def __init__(self):
        super().__init__(
            status_code=self.status_code,
            detail=self.detail
        )


class WrongFormat(BException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Неверный формат файла!'


class MemReady(BException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Такой мем уже существует!'


class IsNotFound(BException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Такого мема не существует'