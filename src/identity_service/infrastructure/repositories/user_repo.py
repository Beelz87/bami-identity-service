import uuid
from typing import Dict, Optional

from identity_service.domain.models.user import User


class UserRepository:
    """
    In-memory user repository.
    Suitable for early development and testing.
    """

    def __init__(self):
        # key: user_id
        self._users: Dict[str, User] = {}

    def get_by_username(self, username: str) -> Optional[User]:
        for user in self._users.values():
            if user.username == username:
                return user
        return None

    def get_by_id(self, user_id: str) -> Optional[User]:
        return self._users.get(user_id)

    def create(
        self,
        username: str,
        password: str,
        roles: list[str]
    ) -> User:
        user_id = str(uuid.uuid4())

        user = User(
            id=user_id,
            username=username,
            password=password,
            roles=roles
        )

        self._users[user_id] = user
        return user
