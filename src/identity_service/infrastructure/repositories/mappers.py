from domain.models.user import UserORM, User


def to_domain(user: UserORM) -> User:
    return User(
        id=str(user.id),
        username=user.username,
        password=user.password,
        roles=user.roles
    )
