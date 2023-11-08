import pytest
from application import *
from application.models import *

# fixture

@pytest.fixture
def client():
    env = "TEST"
    #  initialise a test app
    app = create_app(env)

#  create a test client to which we can make requests
    client = app.test_client()

   

# create a test database with some test data
    with app.app_context():
        db.create_all()
        test_character = FriendsCharacter(name="Test", age=0, catch_phrase="Im a test")
        db.session.add(test_character)
        db.session.commit()
    return client    