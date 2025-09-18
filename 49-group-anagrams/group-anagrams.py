from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            # Make a count of 26 letters
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1  # convert char → index

            # Use tuple(count) as key (hashable)
            anagram_map[tuple(count)].append(word)

        return list(anagram_map.values())
