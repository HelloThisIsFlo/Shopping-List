import pytest
from shoppinglist.cost import CostCalculator, InvalidItem


PRICES = {
    'InWallSwitch': 5,
    'BulbBasic': 10,
    'BulbColor': 55,
}


@pytest.fixture
def calculator():
    calculator = CostCalculator(PRICES)
    return calculator


def test_invalid_item(calculator):
    with pytest.raises(InvalidItem) as e:
        calculator.cost({
            'kitchen': [
                'ThisItemHasNoPrice'
            ]
        })

    assert str(e.value) == "No price found for this item: 'ThisItemHasNoPrice'"


def test_single_room(calculator):
    items_per_room = {
        'kitchen': [
            'InWallSwitch',
            'BulbBasic'
        ]
    }

    res = calculator.cost(items_per_room)

    assert res == {
        'total': 15,
        'rooms': {
            'kitchen': 15
        }
    }


def test_single_room_with_duplicates(calculator):
    items_per_room = {
        'kitchen': [
            'InWallSwitch',
            'InWallSwitch',
            'InWallSwitch',
            'InWallSwitch',
            'BulbBasic'
        ]
    }

    res = calculator.cost(items_per_room)

    assert res == {
        'total': 30,
        'rooms': {
            'kitchen': 30
        }
    }


def test_multiple_rooms(calculator):
    items_per_room = {
        'kitchen': [
            'InWallSwitch',
            'BulbBasic'
        ],
        'living-room': [
            'BulbColor',
            'BulbBasic',
        ]
    }

    res = calculator.cost(items_per_room)

    assert res == {
        'total': 80,
        'rooms': {
            'kitchen': 15,
            'living-room': 65
        }
    }
