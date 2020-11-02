from typing import List

from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        answer = []

        cnt = dict(Counter(nums))
        # print(cnt)
        for num in nums :
            tmp = 1
            tmp_dict = cnt.copy()
            tmp_dict[num] -= 1
            for key, value in tmp_dict.items():
                if value == 0 :
                    continue
                tmp = tmp * (key**value)
            answer.append(tmp)

        return answer

if __name__ == '__main__':
    s = Solution
    nums = [1, 2, 3, 4]
    # nums = [1,0]
    # nums = [1, -1]
    # nums = [2, 3, 5, 0]
    print(s.productExceptSelf(s, nums))