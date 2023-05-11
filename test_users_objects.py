import pytest

from models.providers import UserProvider, CsvUserProvider, DataBaseUserProvider, ApiUserProvider
from models.users import User, UserStatus, Worker


@pytest.fixture(params=[CsvUserProvider(), DataBaseUserProvider(), ApiUserProvider()])
def provider(request) -> UserProvider:
    return request.param


@pytest.fixture
def users(provider) -> list[User]:
    user_models = provider.get_users()
    return user_models


@pytest.fixture
def workers(users) -> list[Worker]:
    return [Worker.from_user(user) for user in users if user.status == UserStatus.Worker]


def assert_workers_are_adults(workers):
    for worker in workers:
        assert worker.is_adult()


def test_workers_are_adults_v2(workers):
    assert_workers_are_adults(workers)