from enum import Enum
from dataclasses import dataclass


class UserStatus(Enum):
    Student = 'student'
    Worker = 'worker'


@dataclass
class User:
    name: str
    age: int
    status: UserStatus
    items: list[str]

    @classmethod
    def from_csv(cls, user_dict):
        return cls(name=user_dict['name'],
                   age=int(user_dict['age']),
                   status=user_dict['status'],
                   items=user_dict['items'])

    def is_adult(self) -> bool:
        return self.age >= 18


class Worker(User):
    def __init__(self, name, age, items):
        super().__init__(name=name, age=age, status=UserStatus.Worker, items=items)

    @classmethod
    def from_user(cls, user: User):
        assert user.status == UserStatus.Worker
        return cls(name=user.name, age=user.age, items=user.items)

    def do_work(self):
        pass


if __name__ == '__main__':
    oleg = User(name='Oleg', age=18, status=UserStatus.Student, items=[])
    assert oleg.is_adult() is True