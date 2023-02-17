class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        # 애너그램 -> 알파벳 순으로 정렬하면 같은 값이 나옴
        for word in strs:   # 알파벳 순으로 정렬한 값을 키로 딕셔너리를 만듦
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())
