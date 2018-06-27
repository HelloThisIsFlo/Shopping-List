import textwrap
import yaml
from .items import CostCalculator, Counter, Formatter


class Main:
    def __init__(self, prices_filename, items_per_category_filename):
        self.formatter = Formatter()
        self.counter = Counter()
        self.prices = self._parse_file(prices_filename)
        self.items_per_category = self._parse_file(items_per_category_filename)

    def _parse_file(self, filename):
        with open(filename) as f:
            return yaml.load(f)

    def process_file(self, with_count=False):
        calculator = CostCalculator(self.prices)
        cost_result = calculator.cost(self.items_per_category)

        if with_count:
            count_result = self.counter.count_items(self.items_per_category)
            return self.formatter.format(cost_result, count_result)
        else:
            return self.formatter.format(cost_result)
