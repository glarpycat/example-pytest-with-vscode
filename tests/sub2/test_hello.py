from hello import greeting_at_noon

def test_hello():
    assert greeting_at_noon("Nikita") == "Good afternoon, Nikita"
