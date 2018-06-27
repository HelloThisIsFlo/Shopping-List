import textwrap
from shoppinglist.main import Main


def test_full_processing():
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

    list_mock_file = './tests/complete_list_mock.yaml'
    prices_mock_file = './tests/prices_mock.yaml'

    main = Main(prices_mock_file, list_mock_file)

    assert main.process_file() == textwrap.dedent("""
            Total cost breakdown
            --------------------
            Kitchen: 50 €
            Living Room: 5 €
            --------------------

            Total: 55 €
            """)

def test_full_processing_with_count():
    list_mock_file = './tests/complete_list_mock.yaml'
    prices_mock_file = './tests/prices_mock.yaml'

    main = Main(prices_mock_file, list_mock_file)

    assert main.process_file(with_count=True) == textwrap.dedent("""
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
