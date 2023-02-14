class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter: list[str] = list(filter(lambda x: x.split(' ')[1].isalpha(), logs))
        digit: list[str] = list(filter(lambda x: x.split(' ')[1].isdigit(), logs))

        letter = sorted(letter, key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

        return letter + digit