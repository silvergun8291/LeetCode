class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = list(filter(lambda x: x not in banned, re.sub(r'\W', ' ', paragraph).lower().split()))
        counters = collections.Counter(words)

        return counters.most_common(1)[0][0]