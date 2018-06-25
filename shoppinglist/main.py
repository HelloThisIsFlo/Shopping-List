import textwrap
import yaml
from shoppinglist.cost import CostCalculator, CostFormatter

def _parse_file(filename):
    with open(filename) as f:
        parsed = yaml.load(f)
        return (parsed['ItemPrices'], parsed['Rooms'])

def process_file(filename):
    prices, items_per_room = _parse_file(filename)

    calculator = CostCalculator(prices)
    formatter = CostFormatter()
    cost_result = calculator.cost(items_per_room)
    return formatter.format(cost_result)
