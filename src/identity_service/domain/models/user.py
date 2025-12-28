from dataclasses import dataclass


@dataclass
class User:
    id: str
    username: str
    password: str
    roles: list[str]
