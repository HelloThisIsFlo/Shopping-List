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

    class TestWithOverrides:
        @pytest.fixture
        def items(self):
            # Without overrides that list should total 80 €
            #
            # - 1 x InWallSwitch =  5 €
            # - 2 x BulbBasic    = 20 €
            # - 1 x BulbColor    = 55 €
            # --------------------------
            #              Total = 80 €
            return {
                'kitchen': [
                    'InWallSwitch',
                    'BulbBasic'
                ],
                'living-room': [
                    'BulbColor',
                    'BulbBasic',
                ]
            }

        def test_simple_override(self, items):  # TODO
            # Given: Price 'InWallSwitch' increase 5 -> 10 €
            with_increased_inwallswitch_price = {'InWallSwitch': 10}

            # When: Calculating price
            calculator = CostCalculator(
                PRICES, (with_increased_inwallswitch_price,))
            result = calculator.cost(items)

            # Then: Total is increase of the corresponding ammount
            assert result['total'] == 85  # 80 + 5 € increase

        def test_override_inexisting(self, items):  # TODO
            # Given: 'BulbColor' price absent from base price, but present in override
            base_prices = PRICES.copy()
            base_prices.pop('BulbColor')
            assert 'BulbColor' not in base_prices
            override_with_bulbcolor_price = {
                'BulbColor': 155  # 100 € more than original pricehl
            }

            # When: Calculating price
            calculator = CostCalculator(
                base_prices, (override_with_bulbcolor_price,))
            result = calculator.cost(items)

            # Then: Total is based on the correct price
            assert result['total'] == 180  # 80 + 100 € increase

        def test_override_two_times(self, items):  # TODO
            # Given: Price 'InWallSwitch' is overrided 2 times
            first_override = {'InWallSwitch': 10}  # 5 € increase
            second_override = {'InWallSwitch': 30}  # 25 € increase

            # When: Calculating price
            calculator = CostCalculator(
                PRICES, (first_override, second_override))
            result = calculator.cost(items)

            # Then: Total is based on the last override
            assert result['total'] == 105  # 80 + 25 € increase


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
