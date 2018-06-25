import textwrap
import pytest
from shoppinglist.cost import CostCalculator, InvalidItem, CostFormatter

PRICES = {
    'InWallSwitch': 5,
    'BulbBasic': 10,
    'BulbColor': 55,
}


class TestCalculator:
    @pytest.fixture
    def calculator(self):
        calculator = CostCalculator(PRICES)
        return calculator

    def test_invalid_item(self, calculator):
        with pytest.raises(InvalidItem) as e:
            calculator.cost({
                'kitchen': [
                    'ThisItemHasNoPrice'
                ]
            })

        assert str(
            e.value) == "No price found for this item: 'ThisItemHasNoPrice'"

    def test_single_room(self, calculator):
        items_per_room = {
            'kitchen': [
                'InWallSwitch',
                'BulbBasic'
            ]
        }

        res = calculator.cost(items_per_room)

        assert res == {
            'total': 15,
            'rooms': [
                ('kitchen', 15)
            ]
        }

    def test_single_room_with_duplicates(self, calculator):
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
            'rooms': [
                ('kitchen', 30)
            ]
        }

    def test_multiple_rooms(self, calculator):
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
            'rooms': [
                ('kitchen', 15),
                ('living-room', 65)
            ]
        }


class TestFormatter:
    @pytest.fixture
    def formatter(self):
        return CostFormatter()

    def test_single_room(self, formatter):
        assert formatter.format({
            'total': 15,
            'rooms': [
                ('kitchen', 15),
            ]
        }) == textwrap.dedent("""
            Total cost breakdown

            ---
            Kitchen: 15 €
            ---

            Total: 15 €
            """)

    def test_single_room_multiple_words(self, formatter):
        assert formatter.format({
            'total': 80,
            'rooms': [
                ('living-room', 80)
            ]
        }) == textwrap.dedent("""
            Total cost breakdown

            ---
            Living Room: 80 €
            ---

            Total: 80 €
            """)

    def test_multiple_rooms(self, formatter):
        assert formatter.format({
            'total': 80,
            'rooms': [
                ('kitchen', 15),
                ('living-room', 65)
            ]
        }) == textwrap.dedent("""
            Total cost breakdown

            ---
            Kitchen: 15 €
            Living Room: 65 €
            ---

            Total: 80 €
            """)