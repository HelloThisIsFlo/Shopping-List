import textwrap
import shoppinglist.main

def test_full_processing():
    mock_file = './tests/complete_list_mock.yaml'

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


    assert shoppinglist.main.process_file(mock_file) == textwrap.dedent("""
            Total cost breakdown

            ---
            Kitchen: 50 €
            Living Room: 5 €
            ---

            Total: 55 €
            """)


