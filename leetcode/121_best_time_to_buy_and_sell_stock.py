from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell, result = 0, 0
        for i in range(len(prices)-1, -1, -1) :
            sell = max(sell, prices[i])
            result = max(result, sell-prices[i])
        return result


if __name__ == '__main__':
    s = Solution
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(s, prices))