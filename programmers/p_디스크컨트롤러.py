import heapq

def solution_3(jobs): # 50점
    answer = 0
    flag = True
    tmp = []
    length = len(jobs)
    for i in range(len(jobs)):
        start, process = jobs[i]
        jobs[i] = [process, start]

    jobs = sorted(jobs, key=lambda x: x[1])
    print(jobs)

    while jobs:
        if flag:
            process, start = jobs.pop(0)
            answer += process
            point = start + process
            flag = False
        else:
            # jobs리스트의 다음 값을 탐색
            if jobs[0][1] >= point:
                jobs = list(jobs)
                process, start = jobs.pop(0)
                answer += process
                point += process
            else:
                heapq.heapify(jobs)
                pre_process, pre_start = process, start
                process, start = heapq.heappop(jobs)
                answer += process
                tmp.append(point - start)
                point += process
    print(tmp)

    return (answer + sum(tmp)) // length

def solution_2(jobs) : # 10점
    answer = 0
    heap = []
    stack = []
    tmp = []
    length = len(jobs)
    flag = False  # stack이 차있고 아직 일이 진행중이라면 False..?

    while True :
        # 처음일때는 그대로 활용
        # 시작시점과 처리시간을 가져오고 그 둘을 더해 새로운 시작시점을 생성
        # 새로운 시작시점을 stack에 넣는다.
        if not stack and not flag:
            start, process = jobs.pop(0)
            start = start + process
            stack.append(start)
            flag = True

        # 현재 작업이 비어있고, heap에 작업이 들어있을때
        # heap에서 작업을 하나 빼온다. -> 빨리 끝나는 작업이 뽑힌다.
        # tmp에는 이전 작업이 끝나기를 기다린 시간(start-next_start) + 다음 작업 처리시간(next_process) 를 저장
        # 시작 시점은 이전에 끝나는 시간과 다음 작업의 처리시간을 합쳐서 새롭게 저장
        # stack에 다시 이 값을 넣어준다.
        elif not stack and heap:
            next_process, next_start = heapq.heappop(heap)
            tmp.append(start - next_start)
            start = start + next_process
            stack.append(start)
            # answer = answer + tmp
            # start = next_start + tmp

        # 현재 작업도 완료, 힙도 비어있고, jobs도 비어 있을 때
        elif not stack and not heap and not jobs :
            break

        # 현재 작업중이면 jobs에서 일을 하나 빼서 힙에 저장
        # 예외처리문을 써서 jobs에서 다 빠져나왔다면 그냥 아무일 없이 진
        else :
            try :
                heap_start, heap_process = jobs.pop(0)
                heapq.heappush(heap, [heap_process, heap_start])
            except:
                pass

        if stack[0]-1 == answer :
            start = stack.pop()

        answer += 1

    # print(tmp)
    # print(sum(tmp))
    return (answer+sum(tmp))//length

def solution(jobs):  # 15점
    answer = 0

    heap = []
    length = len(jobs)

    # 맨 앞에 있는 작업 먼저 뽑기
    prev_start, prev_process = jobs.pop(0)
    answer += prev_process
    prev_start = prev_process

    # 그 뒤의 일은 큐에 삽입
    for a, b in jobs :
        heapq.heappush(heap, [b, a])

    # 큐를 하나씩 뽑는 작업
    while heap :
        # print("jj")
        next_process, next_start = heapq.heappop(heap)
        # print(next_start, next_process)
        # print("pre_s : {}, nex_st: {}, nes_pr : {}".format(prev_start, next_start, next_process))
        tmp = prev_start - next_start + next_process
        answer = answer + tmp
        prev_start = next_start + tmp

    return answer // length

if __name__ == '__main__':
    jobs = [[0, 3], [1, 9], [2, 6]]
    # jobs = [[0, 2], [2, 2], [4, 2]]
    # jobs = [[0, 2], [3, 2], [7, 2]]
    # jobs = [[0, 3], [1, 4], [6, 1]]  # 이 경우에는? 실패
    print(solution_3(jobs))