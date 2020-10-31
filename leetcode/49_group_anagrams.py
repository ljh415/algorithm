
from typing import List

from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = {}
        answer = []
        flag = [False] * len(strs)

        # 딕셔너리 생성
        for idx, str in enumerate(strs):
            tmp_dict[idx] = [str, Counter(str)]

        for i in range(0, len(tmp_dict.keys())):

            if flag[i] == True :
                continue
            flag[i] = True
            tmp = [tmp_dict[i][0]]
            for j in range(i+1, len(tmp_dict.keys())):
                if flag[j] == True :
                    continue
                if tmp_dict[i][1] == tmp_dict[j][1]:
                    flag[j] = True
                    tmp.append(tmp_dict[j][0])
            answer.append(list(tmp))

        # for i in range(len(answer)) :
        #     answer[i] = sorted(answer[i], reverse=False)

        answer = sorted(answer, key=lambda x : len(x))

        return answer

if __name__ == '__main__':
    s=Solution
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # strs = ["",""]
    print(s.groupAnagrams(s, strs))