import textwrap
from shoppinglist.main import Main

LIST_MOCK_FILE = './tests/mocks/shopping_list.yaml'
LIST_WITH_EXTRA_ITEM_MOCK_FILE = './tests/mocks/shopping_list_with_extra_item.yaml'
PRICES_MOCK_FILE = './tests/mocks/prices.yaml'
PRICE_FIRST_OVERRIDE_MOCK_FILE = './tests/mocks/first_override.yaml'
PRICE_SECOND_OVERRIDE_MOCK_FILE = './tests/mocks/second_override.yaml'


def test_basic():
    # Kitchen:
    #   - InWallSwitch <- 10€
    #   - InWallSwitch <- 10€
    #   - PaddleSwitch <- 25€
    #   - MotionSensor <-  5€
    #
    # Living-Room:
    #   - MotionSensor <-  5€
    #
    # ==> Total = 55 € | Kitchen = 50 € | Living Room = 5 €

    main = Main(LIST_MOCK_FILE, PRICES_MOCK_FILE)

    assert main.process_files() == textwrap.dedent("""
            Total cost breakdown
            --------------------
            Kitchen: 50 €
            Living Room: 5 €
            --------------------

            Total: 55 €
            """)


def test_with_count():
    main = Main(LIST_MOCK_FILE, PRICES_MOCK_FILE)

    assert main.process_files(with_count=True) == textwrap.dedent("""
            Total cost breakdown
            --------------------
            Kitchen: 50 €
            Living Room: 5 €
            --------------------

            Item Count
            --------------------
            InWallSwitch: 2
            PaddleSwitch: 1
            MotionSensor: 2
            --------------------

            Total: 55 €
            """)


def test_with_overrides():
    pass
