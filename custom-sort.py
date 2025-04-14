class Solution:
    def customSortString(self, order: str, s: str) -> str:
        freq = {}
        result = ""

        for letter in s:
            freq[letter] = freq.get(letter, 0) + 1

        for character in order:
            if character in freq:
                result += character * freq[character]
                del freq[character]  # Remove it since it's been handled

        # Add the rest of the characters that were not in 'order'
        for character in freq:
            result += character * freq[character]

        return result