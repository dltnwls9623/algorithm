class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = {}
        for s in strs:
            key = ''.join(sorted(s))
            anagrams[key] = anagrams.get(key, []) + [s]

        return anagrams.values()