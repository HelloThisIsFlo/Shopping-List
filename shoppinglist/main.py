import textwrap
import yaml
from shoppinglist.cost import CostCalculator, CostFormatter


class Main:
    def __init__(self, filename):
        self.filename = filename
        self.formatter = CostFormatter()
        self.prices = {}
        self.items_per_room = {}

    def _setup_calculator_with_prices(self):
        self.calculator = CostCalculator(self.prices)

    def _parse_file(self):
        with open(self.filename) as f:
            parsed = yaml.load(f)
            self.prices = parsed['ItemPrices']
            self.items_per_room = parsed['Rooms']

    def process_file(self):
        self._parse_file()
        self._setup_calculator_with_prices()

        cost_result = self.calculator.cost(self.items_per_room)
        return self.formatter.format(cost_result)
