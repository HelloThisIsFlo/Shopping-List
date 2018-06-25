class InvalidItem(Exception):
    pass


class CostCalculator:
    """

    Calculates the cost of times

    Warning: NOT Thread Safe!
    """
    def __init__(self, prices):
        self.prices = prices

    def cost(self, items_per_room):
        self.items_per_room = items_per_room
        self._ensure_valid_items()

        total = 0
        rooms = {}
        for room in items_per_room:
            room_total = self._calculate_room_total(room)
            rooms[room] = room_total
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
                    raise InvalidItem("No price found for this item: '" + item + "'")
