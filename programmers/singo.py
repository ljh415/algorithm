# https://programmers.co.kr/learn/courses/30/lessons/92334?language=python3
from collections import defaultdict, Counter

def solution(id_list, report, k):
    answer = []
    
    total_dict = defaultdict(set)
    for member in id_list:
        total_dict[member]
    
    for rep in report:
        reporter, reported = rep.split(" ")
        total_dict[reporter].add(reported)
        
    report_cnt = defaultdict(int)
    for reporter in total_dict:
        for reported in total_dict[reporter] :
            report_cnt[reported]+=1
    
    for reporter in total_dict:
        cnt = 0
        for reported in total_dict[reporter]:
            if reported in report_cnt:
                if report_cnt[reported] >= k:
                    cnt+=1
        answer.append(cnt)
    
    return answer
'''
 테스트 1 〉	통과 (0.01ms, 10.3MB)
 테스트 2 〉	통과 (0.02ms, 10.2MB)
 테스트 3 〉	통과 (137.30ms, 44.2MB)
 테스트 4 〉	통과 (0.04ms, 10.2MB)
 테스트 5 〉	통과 (0.04ms, 10.4MB)
 테스트 6 〉	통과 (0.94ms, 10.5MB)
 테스트 7 〉	통과 (1.93ms, 10.6MB)
 테스트 8 〉	통과 (3.22ms, 10.9MB)
 테스트 9 〉	통과 (61.14ms, 26.7MB)
테스트 10 〉	통과 (59.98ms, 26.3MB)
테스트 11 〉	통과 (133.68ms, 44.3MB)
테스트 12 〉	통과 (0.26ms, 10.4MB)
테스트 13 〉	통과 (0.27ms, 10.4MB)
테스트 14 〉	통과 (54.25ms, 23.4MB)
테스트 15 〉	통과 (98.78ms, 38.5MB)
테스트 16 〉	통과 (0.15ms, 10.3MB)
테스트 17 〉	통과 (0.25ms, 10.1MB)
테스트 18 〉	통과 (0.58ms, 10.2MB)
테스트 19 〉	통과 (0.67ms, 10.4MB)
테스트 20 〉	통과 (72.92ms, 23.3MB)
테스트 21 〉	통과 (104.39ms, 38.6MB)
테스트 22 〉	통과 (0.01ms, 10.2MB)
테스트 23 〉	통과 (0.01ms, 10.2MB)
테스트 24 〉	통과 (0.01ms, 10.1MB)
'''

def solution2(id_list, report, k):
    answer = []
    
    total_dict = defaultdict(set)
    for member in id_list:
        total_dict[member]
    
    for rep in report:
        reporter, reported = rep.split(" ")
        total_dict[reporter].add(reported)
        
    total_report= []
    for member, reported in total_dict.items():
        total_report.extend(list(reported))
    total_report = dict(Counter(total_report))
    ban_member = [reported for reported, report_num in total_report.items() if report_num >= k]

    for member in total_dict:
        cnt = 0
        for reported in total_dict[member]:
            if reported in ban_member:
                cnt+=1
        answer.append(cnt)
    
    return answer
'''
 테스트 1 〉	통과 (0.04ms, 10.2MB)
 테스트 2 〉	통과 (0.04ms, 10.2MB)
 테스트 3 〉	통과 (1158.12ms, 45.7MB)
 테스트 4 〉	통과 (0.06ms, 10.2MB)
 테스트 5 〉	통과 (0.06ms, 10MB)
 테스트 6 〉	통과 (0.96ms, 10.6MB)
 테스트 7 〉	통과 (2.16ms, 10.7MB)
 테스트 8 〉	통과 (3.77ms, 11MB)
 테스트 9 〉	통과 (302.58ms, 27MB)
테스트 10 〉	통과 (58.97ms, 26.9MB)
테스트 11 〉	통과 (624.81ms, 45.6MB)
테스트 12 〉	통과 (0.86ms, 10.3MB)
테스트 13 〉	통과 (0.30ms, 10.4MB)
테스트 14 〉	통과 (393.40ms, 23.9MB)
테스트 15 〉	통과 (112.93ms, 39MB)
테스트 16 〉	통과 (0.20ms, 10.4MB)
테스트 17 〉	통과 (0.29ms, 10.3MB)
테스트 18 〉	통과 (0.71ms, 10.2MB)
테스트 19 〉	통과 (1.25ms, 10.4MB)
테스트 20 〉	통과 (359.14ms, 24MB)
테스트 21 〉	통과 (596.00ms, 39.1MB)
테스트 22 〉	통과 (0.04ms, 10.1MB)
테스트 23 〉	통과 (0.03ms, 10.2MB)
테스트 24 〉	통과 (0.03ms, 10.3MB)
'''


if __name__ == '__main__':
    input_args = [
        (["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2),
        (["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3),
    ]
    for id_list, report, k in input_args:
        solution2(id_list, report, k)
        print()