from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        answer = []
        l_log, d_log = [], []

        for i in range(len(logs)-1, -1, -1) :
            if not logs[i].split()[1].isnumeric():
                l_log.append(logs.pop(i))
            else:
                continue

        l_log.sort(key=lambda x : x.split()[1:])
        l_log.extend(logs)

        return l_log

if __name__ == '__main__':

    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    s = Solution
    print(s.reorderLogFiles(s, logs))