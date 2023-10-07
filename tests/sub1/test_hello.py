from hello import greeting
from user import User


def test_hello():
    user = User("Nikita", "nikita@example.com")
    assert greeting(user) == "Hello, Nikita"
