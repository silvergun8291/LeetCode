class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 주어진 문자열 자체가 팰린드롬이면 바로 리턴
        if len(s) < 2 or s == s[::-1]:
            return s

        result: str = ''
        for i in range(len(s)):     # 슬라이딩 윈도우 방식으로 가장 긴 부분 팰린드롬 탐색
            result = max(result, self.expand(s, i, i + 1), self.expand(s, i, i + 2), key=len)

        return result

    def expand(self, s: str, left: int, right: int):
        # 중앙을 중심으로 투 포인트 확장하여 가장 긴 팰린드롬 찾기
        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1

        # while 문의 내용이 실행된 후 종료 되기 때문에 left, right 를 -1 한 값을 리턴
        return s[left+1:right] 