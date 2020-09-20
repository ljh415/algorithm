def solution(numbers, target):
    answer = 0
    len_numbers = len(numbers)
    # DFS같은데 내려가는 순서가 조금 다른거 같다...
    def operator(idx=0) :
        if idx < len_numbers:
            numbers[idx] *= 1
            operator(idx+1)

            numbers[idx] *= -1
            operator(idx+1)

        elif sum(numbers) == target :
            nonlocal answer
            answer += 1

    operator()

    return answer

######

def dfs (array, numbers, target, size):
    answer = 0
    if len(array) == size:
        if sum(array) == target:
            return 1
        else:
            return 0
    else :
        A = numbers.pop(0)
        for i in [1, -1]:
            array.append(A * i)
            answer += dfs(array, numbers, target, size)
            array.pop()
        numbers.append(A)
        return answer

def solution_dfs(numbers, target):
    answer = 0
    answer += dfs([numbers[0]], numbers[1:], target, len(numbers))
    answer += dfs([-numbers[0]], numbers[1:], target, len(numbers))

    return answer

#####
# 완전탐색
from itertools import product
def solution_brute(numbers, tareget):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

####
# bfs
import collections
def solution_bfs(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack :
        current_sum, num_idx = stack.popleft()

        if num_idx  == len(numbers) :
            if current_sum == target:
                answer += 1
            else :
                number = numbers[num_idx]
                stack.append((current_sum+number, num_idx+1))
                stack.append((current_sum-number, num_idx+1))

    return answer

#####
# dfs2

answer = 0
def DFS(idx, numbers, target, value) :
    global answer
    N = len(nubers)
    if (idx == N and target == value):
        answer += 1
        return
    if (idx==n):
        return

    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution_dfs2(numbers, target):
    global answer
    DFS(0, numbers, target, 0)
    return answer


if __name__ == '__main__':
    numbers, target = [1, 1, 1, 1, 1], 3

    print(solution_dfs(numbers, target))