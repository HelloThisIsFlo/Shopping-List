import collections
import textwrap


class InvalidItem(Exception):
    pass


class CostCalculator:
    """

    Calculates the cost of items

    Warning: NOT Thread Safe!
    """

    def __init__(self, prices, price_overrides=()):
        self.prices = self._compute_final_price(prices, price_overrides)

    @staticmethod
    def _compute_final_price(base_prices, price_overrides):
        final_prices = base_prices.copy()
        for price_override in price_overrides:
            for item in price_override:
                final_prices[item] = price_override[item]

        return final_prices

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
    def format(self, cost_result, count_result={}, show_breakdown=True):
        self.cost_result = cost_result
        self.count_result = count_result
        self.show_breakdown = show_breakdown

        breakdown = self._format_breakdown()
        count = self._format_count()
        total = self._format_total()

        return breakdown + count + total

    def _format_breakdown(self):
        if not self.show_breakdown:
            return ""

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

    def _format_count(self):
        if self.count_result == {}:
            return ""

        header = textwrap.dedent("""
            Item Count
            --------------------""")
        content = self._format_count_content()
        footer = textwrap.dedent("""
            --------------------
            """)

        return header + content + footer

    def _format_count_content(self):
        formatted_count = ['']
        for item in self.count_result:
            count = self.count_result[item]
            formatted_count.append(f"{item}: {count}")

        return '\n'.join(formatted_count)

    @staticmethod
    def _format_category_name(category_name):
        return ' '.join(list(map(
            lambda n: n.capitalize(),
            category_name.split('-'))))

    def _format_total(self):
        return textwrap.dedent(f"""
            Total: {self.cost_result['total']} €
            """)
