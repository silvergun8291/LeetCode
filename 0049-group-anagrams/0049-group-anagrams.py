class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)
        print(anagrams)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())