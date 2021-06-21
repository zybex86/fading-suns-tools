import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_character_model():
    character = baker.make(
        'characters.Character',
        name='Lucifer Morningstar',
        player='John Doe'
    )
    assert str(character) == 'John Doe - Lucifer Morningstar (WIP)'
