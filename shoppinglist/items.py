import collections
import textwrap


class InvalidItem(Exception):
    pass


class CostCalculator:
    """

    Calculates the cost of items

    Warning: NOT Thread Safe!
    """

    def __init__(self, prices):
        self.prices = prices

    def cost(self, items_per_category):
        self.items_per_category = items_per_category
        self._ensure_valid_items()

        total = 0
        categories = []
        for category in items_per_category:
            category_total = self._calculate_category_total(category)
            categories.append((category, category_total))
            total += category_total

        return {
            'total': total,
            'categories': categories
        }

    def _calculate_category_total(self, category):
        total = 0
        for item in self.items_per_category[category]:
            price = self.prices[item]
            total += price
        return total

    def _ensure_valid_items(self):
        for category in self.items_per_category:
            for item in self.items_per_category[category]:
                if item not in self.prices:
                    raise InvalidItem(
                        "No price found for this item: '" + item + "'")


class Counter:
    def __init__(self):
        pass

    def count_items(self, items_per_category):
        count_result = {}
        for category in items_per_category:
            for item in items_per_category[category]:
                if item in count_result:
                    count_result[item] += 1
                else:
                    count_result[item] = 1

        return count_result


class Formatter:
    def format(self, cost_result, count_result={}):
        self.cost_result = cost_result

        breakdown = self._format_breakdown()
        footer_total = self._format_footer_total()

        return breakdown + footer_total

    def _format_breakdown(self):
        header = textwrap.dedent("""
            Total cost breakdown
            --------------------""")
        content = self._format_breakdown_content()
        footer = textwrap.dedent("""
            --------------------
            """)

        return header + content + footer

    def _format_breakdown_content(self):
        formatted_categories = ['']
        for (category, cost) in self.cost_result['categories']:
            formatted_category_name = self._format_category_name(category)
            formatted_categories.append(f"{formatted_category_name}: {cost} €")

        return '\n'.join(formatted_categories)

    @staticmethod
    def _format_category_name(category_name):
        return ' '.join(list(map(
            lambda n: n.capitalize(),
            category_name.split('-'))))

    def _format_footer_total(self):
        return textwrap.dedent(f"""
            Total: {self.cost_result['total']} €
            """)
