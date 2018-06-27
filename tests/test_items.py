import textwrap
import pytest
from shoppinglist.items import CostCalculator, InvalidItem, Counter, Formatter

PRICES = {
    'InWallSwitch': 5,
    'BulbBasic': 10,
    'BulbColor': 55,
}


class TestCostCalculator:
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

    def test_single_category(self, calculator):
        items_per_category = {
            'kitchen': [
                'InWallSwitch',
                'BulbBasic'
            ]
        }

        res = calculator.cost(items_per_category)

        assert res == {
            'total': 15,
            'categories': [
                ('kitchen', 15)
            ]
        }

    def test_single_category_with_duplicates(self, calculator):
        items_per_category = {
            'kitchen': [
                'InWallSwitch',
                'InWallSwitch',
                'InWallSwitch',
                'InWallSwitch',
                'BulbBasic'
            ]
        }

        res = calculator.cost(items_per_category)

        assert res == {
            'total': 30,
            'categories': [
                ('kitchen', 30)
            ]
        }

    def test_multiple_categories(self, calculator):
        items_per_category = {
            'kitchen': [
                'InWallSwitch',
                'BulbBasic'
            ],
            'living-room': [
                'BulbColor',
                'BulbBasic',
            ]
        }

        res = calculator.cost(items_per_category)

        assert res == {
            'total': 80,
            'categories': [
                ('kitchen', 15),
                ('living-room', 65)
            ]
        }


class TestCounter:
    @pytest.fixture
    def counter(self):
        return Counter()

    def test_multiple_categories(self, counter):
        items_per_category = {
            'kitchen': [
                'InWallSwitch',
                'BulbBasic'
            ],
            'living-room': [
                'BulbColor',
                'BulbBasic',
            ]
        }
        res = counter.count_items(items_per_category)

        assert res == {
            'InWallSwitch': 1,
            'BulbBasic': 2,
            'BulbColor': 1
        }


class TestFormatter:
    @pytest.fixture
    def formatter(self):
        return Formatter()

    class TestWithoutCount:
        def test_single_category(self, formatter):
            assert formatter.format({
                'total': 15,
                'categories': [
                    ('kitchen', 15),
                ]
            }) == textwrap.dedent("""
                Total cost breakdown
                --------------------
                Kitchen: 15 €
                --------------------

                Total: 15 €
                """)

        def test_single_category_multiple_words(self, formatter):
            assert formatter.format({
                'total': 80,
                'categories': [
                    ('living-room', 80)
                ]
            }) == textwrap.dedent("""
                Total cost breakdown
                --------------------
                Living Room: 80 €
                --------------------

                Total: 80 €
                """)

        def test_multiple_categories(self, formatter):
            assert formatter.format({
                'total': 80,
                'categories': [
                    ('kitchen', 15),
                    ('living-room', 65)
                ]
            }) == textwrap.dedent("""
                Total cost breakdown
                --------------------
                Kitchen: 15 €
                Living Room: 65 €
                --------------------

                Total: 80 €
                """)

    class TestWithCount:
        def test_multiple_categories(self, formatter):
            formatted = formatter.format(
                {
                    'total': 80,
                    'categories': [
                        ('kitchen', 15),
                        ('living-room', 65)
                    ]
                }, {
                    'InWallSwitch': 1,
                    'BulbBasic': 2,
                    'BulbColor': 1
                })

            assert formatted == textwrap.dedent("""
                Total cost breakdown
                --------------------
                Kitchen: 15 €
                Living Room: 65 €
                --------------------

                Item Count
                --------------------
                InWallSwitch: 1
                BulbBasic: 2
                BulbColor: 1
                --------------------

                Total: 80 €
                """)
