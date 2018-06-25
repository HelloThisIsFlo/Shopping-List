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
    mock_file = './tests/complete_list_mock.yaml'
    main = Main(mock_file)
    assert main.process_file() == textwrap.dedent("""
            Total cost breakdown

            ---
            Kitchen: 50 €
            Living Room: 5 €
            ---

            Total: 55 €
            """)
