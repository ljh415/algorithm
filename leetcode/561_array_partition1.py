from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        answer = 0
        nums = sorted(nums)

        for i in range(len(nums)):
            if i % 2 == 0 :
                tmp = nums[i]
            else :
                answer = answer + min(tmp, nums[i])
        return answer

if __name__ == '__main__':
    s = Solution
    # nums = [1,4,3,2]
    nums = [6,2,6,5,1,2]
    print(s.arrayPairSum(s, nums))