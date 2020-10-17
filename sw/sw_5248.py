'''
unioin find 문제
부모를 저장하는 배열을 만든 뒤에 조가 만들어질 때 작은 번호를 가진 쪽으로 부모를 병합하는 과정
부모를 찾을 때는 재귀를 이용하여 찾도록 한다.
마지막에 데이터가 최산화 되어있지 않을수도 있기 때문에 Set을 만들어 모든 부모노드를 넣어준다.
부모가 다를 경우 다른 조라고 판단.
부모를 표시하는 리스트를 만들 때 N+1까지 만들었기 때문에 set에 0이 추가된다.

따라서 결과값을 출력할 때 -1을 해준다.
'''
def solution_1() :
    def get_parent(x) :
        if parent[x] != x :
            parent[x] = get_parent(parent[x])
        return parent[x]

    def union_parent(x, y):
        a = get_parent(x)
        b = get_parent(y)
        if a > b :
            parent[a] = b
        else :
            parent[b] = a

    for t in range(int(input())):
        N, M = map(int, input().split())
        parent = [i for i in range(N+1)]
        votes = list(map(int, input().split()))

        for i in range(0, M*2, 2) :
            union_parent(votes[i], votes[i+1])
        answer = set()

        for i in parent :
            answer.add(get_parent(i))

        print(f'#{t+1} {len(answer)-1}')

###
def solution_2() :
    def find_set(x) :
        if x == parent[x] :
            return x
        else:
            return find_set(parent[x])

    def union(x, y) :
        parent[find_set(y)] = find_set(x)

    TC = int(input())
    for tc in range(1, TC+1):
        N, M = map(int, input().split())
        parent = [i for i in range(N+1)]
        print(parent)
        init_data = list(map(int, input().split()))
        for i in range(M) :
            start = init_data[2*1]
            end = init_data[2*i+1]
            union(start, end)

        result = []
        for i in range(len(parent)) :
            result.append(find_set(i))

        print(f'#{tc} {len(set(result))-1}')

if __name__ == '__main__':
    solution_2()
