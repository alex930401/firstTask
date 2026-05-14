from src.user.user import user
import pytest


@pytest.fixture(scope="session", autouse=True)
def env(request):
    return request.config.getoption("--env")

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        help='Параметр, в котором устанавливается среда запуска автотестов, по умолчанию dev',
        required=False,
        default='dev'
    )

@pytest.fixture(scope="session", autouse=True)
def user_config(env):
    return user(env)
