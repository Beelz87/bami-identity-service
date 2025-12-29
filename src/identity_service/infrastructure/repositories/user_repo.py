from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from identity_service.domain.models.user import UserORM, User
from identity_service.infrastructure.repositories.mappers import to_domain


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_username(self, username: str) -> User | None:
        user = (
            self.session
            .query(UserORM)
            .filter(UserORM.username == username)
            .one_or_none()
        )
        return to_domain(user) if user else None

    def get_by_id(self, user_id: str) -> User | None:
        user = (
            self.session
            .query(UserORM)
            .filter(UserORM.id == user_id)
            .one_or_none()
        )
        return to_domain(user) if user else None

    def create(
        self,
        username: str,
        password: str,
        roles: list[str],
        tenant_id: str,
    ) -> User:
        user = UserORM(
            username=username,
            password=password,
            roles=roles
        )

        self.session.add(user)
        try:
            self.session.commit()
        except IntegrityError:
            self.session.rollback()
            raise

        self.session.refresh(user)
        return to_domain(user)
