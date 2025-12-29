import uuid
from dataclasses import dataclass

from bami_chassis.infrastructure.database.base import Base
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import Mapped, mapped_column


@dataclass
class User:
    id: str
    username: str
    password: str
    roles: list[str]


class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=False,
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    roles: Mapped[list[str]] = mapped_column(
        JSONB,
        nullable=False,
    )
