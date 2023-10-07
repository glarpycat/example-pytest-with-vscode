from hello import greeting_at_night


def test_hello():
    assert greeting_at_night("Nikita") == "Good night, Nikita"
