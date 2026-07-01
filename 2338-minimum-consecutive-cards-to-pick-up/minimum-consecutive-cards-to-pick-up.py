class Solution:
    def minimumCardPickup(self, cards: list[int]) -> int:
        last_seen = {}
        min_cards = float('inf')
        for i, card in enumerate(cards):
            if card in last_seen:
                current_distance = i - last_seen[card] + 1
                min_cards = min(min_cards, current_distance)
            last_seen[card] = i
        return min_cards if min_cards != float('inf') else -1