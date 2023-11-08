from application.models import *

def test_new_character():
    character = FriendsCharacter("Joe", 12, "I am a great person") 

    assert character.name == "Joe"
    assert character.age == 12
    assert character.catch_phrase == "I am a great person"