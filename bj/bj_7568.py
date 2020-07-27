'''N = int(input())
person = []
height, weight, rank = [0]*N, [0]*N, [0]*N


for i in range(N) :
    weight[i], height[i] = map(int, input().split())

# 일단 새로운 for문에 만들어 본다, 나중에 위에꺼랑 합치든지
cur = [weight[0], height[0]]
rank[0] = 1

for j in range(1, N) :

    # 다음 값이 현재 값보다 클경우
    if cur[0] < weight[j] and cur[1] < height[j] :
        rank[j] = 1
        for k in range(j-1) :
            rank[k] += 1


    # 다음값보다 현재값이 더 클 경우
    else :
        rank[j]



print(height, weight, rank)'''

num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")

# 출처 : https://claude-u.tistory.com/122