class Solution:
    def isPalindrome(self, s: str) -> bool:
        flag = False
        s = s.lower()
        s = list(s)


        for i in range(len(s)-1, -1, -1) :
            if not s[i].isalnum():
                del s[i]

        if not s :
            return True
        elif len(s) == 1:
            return True

        for i in range(len(s)//2) :
            if s[i] != s[len(s)-1-i] :
                return False
            else :
                flag = True
        return flag

if __name__ == '__main__':
    solution = Solution
    # s = "A man, a plan, a canal: Panama"
    s = "race a car"
    print(solution.isPalindrome(solution, s))