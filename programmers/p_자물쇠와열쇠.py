# 자물쇠 => N x N, 열쇠 => M x M
# 격자 형태의 모양
# 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리게 되는 구조
# 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만, 자물쇠 영역 내에서는
# 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.
# 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.

# key를 회전시키는 함수
def rotate(arr) :
    pass

# key를 이동시키는 함수
def shift(arr) :
    pass

# key와 lock을 비교해서 or 연산을 수행..?
def check(arr1, arr2) :
    pass


def solution(key, lock):
    answer = True


    return answer

if __name__ == '__main__':
    key, lock = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

    print(solution(key, lock))