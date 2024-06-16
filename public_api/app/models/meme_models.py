from sqlalchemy.orm import Mapped, mapped_column

from public_api.app.db.config import Base


class Images(Base):
    __tablename__ = 'memes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    url_image: Mapped[str] = mapped_column(nullable=False)
