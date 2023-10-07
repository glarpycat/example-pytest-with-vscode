import time

from user import User


def greeting(user: User):
    time.sleep(3)
    return f"Hello, {user.name}"


def greeting_at_noon(name):
    return f"Good afternoon, {name}"


def greeting_at_night(name):
    return f"Good night, {name}"
