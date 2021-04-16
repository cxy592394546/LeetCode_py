from functools import cache


@cache
def isScramble(s1: str, s2: str) -> bool:
    if sorted(s1) != sorted(s2):
        return False

    if s1 == s2:
        return True

    for i in range(1, len(s1)):
        if (isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:])) or (
                isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i])):
            return True

    return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return isScramble(s1, s2)
