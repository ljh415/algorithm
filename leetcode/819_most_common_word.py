from typing import List

import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        answer =''
        print(paragraph)
        paragraph = paragraph.lower()
        paragraph = re.sub('[^a-zA-Z0-9]', ' ', paragraph).split()
        cnt = dict(Counter(paragraph))

        for key, value in sorted(cnt.items(), key=lambda x: x[1], reverse=True):
            if key not in banned:
                return key

if __name__ == '__main__':
    s = Solution
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(s.mostCommonWord(s, paragraph, banned))