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

    def cost(self, items_per_room):
        self.items_per_room = items_per_room
        self._ensure_valid_items()

        total = 0
        rooms = []
        for room in items_per_room:
            room_total = self._calculate_room_total(room)
            rooms.append((room, room_total))
            total += room_total

        return {
            'total': total,
            'rooms': rooms
        }

    def _calculate_room_total(self, room):
        total = 0
        for item in self.items_per_room[room]:
            price = self.prices[item]
            total += price
        return total

    def _ensure_valid_items(self):
        for room in self.items_per_room:
            for item in self.items_per_room[room]:
                if item not in self.prices:
                    raise InvalidItem(
                        "No price found for this item: '" + item + "'")


class Formatter:
    def format(self, cost_result):
        self.cost_result = cost_result

        header_title = self._format_header_title()
        rooms = self._format_rooms()
        footer_total = self._format_footer_total()

        return header_title + rooms + footer_total

    def _format_header_title(self):
        return textwrap.dedent("""
            Total cost breakdown

            ---""")

    def _format_rooms(self):
        formatted_rooms = ['']
        for (room, cost) in self.cost_result['rooms']:
            formatted_room_name = self._format_room_name(room)
            formatted_rooms.append(f"{formatted_room_name}: {cost} €")

        return '\n'.join(formatted_rooms)

    @staticmethod
    def _format_room_name(room_name):
        return ' '.join(list(map(
            lambda n: n.capitalize(),
            room_name.split('-'))))

    def _format_footer_total(self):
        return textwrap.dedent(f"""
            ---

            Total: {self.cost_result['total']} €
            """)
