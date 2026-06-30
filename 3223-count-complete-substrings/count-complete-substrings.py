class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        total_complete = 0
        i = 0
        while i < n:
            j = i + 1
            while j < n and abs(ord(word[j]) - ord(word[j-1])) <= 2:
                j += 1
            segment = word[i:j]
            for unique_chars in range(1, 27):
                window_len = unique_chars * k
                
                if window_len > len(segment):
                    break
                counts = [0] * 26
                chars_with_k = 0
                for w_end in range(len(segment)):
                    # Add new character to window
                    char_idx = ord(segment[w_end]) - ord('a')
                    counts[char_idx] += 1
                    if counts[char_idx] == k:
                        chars_with_k += 1
                    elif counts[char_idx] == k + 1:
                        chars_with_k -= 1
                    if w_end >= window_len:
                        old_char_idx = ord(segment[w_end - window_len]) - ord('a')
                        counts[old_char_idx] -= 1
                        if counts[old_char_idx] == k:
                            chars_with_k += 1
                        elif counts[old_char_idx] == k - 1:
                            chars_with_k -= 1
                    if w_end >= window_len - 1 and chars_with_k == unique_chars:
                        total_complete += 1
            i = j
        return total_complete