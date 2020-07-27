T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    list_len  = int(input())
    in_value = list(map(int, ((input().split(' ')))))
    min_value = min(in_value)
    max_value = max(in_value)
    result = max_value - min_value
    print("#{} {}".format(test_case, result))