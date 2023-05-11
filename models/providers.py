from models.users import User
import csv


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError('Реализуйте эту функцию в конкретном провайдере')


class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        with open('users.csv') as f:
            user_dicts = list(csv.DictReader(f, delimiter=';'))
        user_models = []
        for user in user_dicts:
            user_models.append(User.from_csv(user))
        return user_models


class DataBaseUserProvider(UserProvider):
    pass


class ApiUserProvider(UserProvider):
    pass