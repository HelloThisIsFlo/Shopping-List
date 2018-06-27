import textwrap
import yaml
from .items import CostCalculator, Counter, Formatter


class Main:
    def __init__(self, items_per_category_filename, prices_filename, price_overrides_filenames=()):
        self.formatter = Formatter()
        self.counter = Counter()
        self.prices = self._parse_file(prices_filename)
        self.price_overrides = self._parse_price_overrides(
            price_overrides_filenames)
        self.items_per_category = self._parse_file(items_per_category_filename)

    def _parse_file(self, filename):
        with open(filename) as f:
            return yaml.load(f)

    def _parse_price_overrides(self, price_overrides_filenames):
        price_overrides = []
        for price_override_filename in price_overrides_filenames:
            price_overrides.append(self._parse_file(price_override_filename))

        return tuple(price_overrides)

    def process_files(self, with_count=False):
        calculator = CostCalculator(self.prices, self.price_overrides)
        cost_result = calculator.cost(self.items_per_category)

        if with_count:
            count_result = self.counter.count_items(self.items_per_category)
            return self.formatter.format(cost_result, count_result)
        else:
            return self.formatter.format(cost_result)
