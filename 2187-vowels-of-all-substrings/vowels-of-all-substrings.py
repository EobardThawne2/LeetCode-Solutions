class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set('aeiou')
        total_vowels = 0
        n = len(word)
        for i, char in enumerate(word):
            if char in vowels:
                total_vowels += (i + 1) * (n - i)
        return total_vowels