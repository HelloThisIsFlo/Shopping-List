import textwrap
import yaml
from .cost import CostCalculator, CostFormatter


class Main:
    def __init__(self, prices_filename, items_per_room_filename):
        self.formatter = CostFormatter()
        self.prices = self._parse_file(prices_filename)
        self.items_per_room = self._parse_file(items_per_room_filename)

    def _parse_file(self, filename):
        with open(filename) as f:
            return yaml.load(f)

    def process_file(self):
        calculator = CostCalculator(self.prices)
        cost_result = calculator.cost(self.items_per_room)
        return self.formatter.format(cost_result)
