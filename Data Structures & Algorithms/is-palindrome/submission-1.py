class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cleaned = "".join([char for char in s if char.isalnum()]).lower()
        s = 0
        e = len(cleaned) - 1

        while s <= e:
            if s == e:
                return True
            if cleaned[s] == cleaned[e]:
                s += 1
                e -= 1
            else:
                return False
        return True