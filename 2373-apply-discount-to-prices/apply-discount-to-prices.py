class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        multiplier = (100 - discount) / 100.0
        for i, word in enumerate(words):
            if len(word) > 1 and word[0] == '$' and word[1:].isdigit():
                new_price = int(word[1:]) * multiplier
                words[i] = f"${new_price:.2f}"
        return " ".join(words)