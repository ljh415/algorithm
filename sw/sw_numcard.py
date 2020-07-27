from collections import Counter

t = int(input())

for x in range(t) :

    # 테스트 케이스가 바뀌면서 변수 초기화
    max_num, key_lst = 0, []

    n = int(input())

    # str으로 입력 받은 것을 list로 형변환
    in_num = list(input())
    # cnt에 counter 객체 저장
    cnt = Counter(in_num)
    # cnt를 value값을 기준으로 내림차순으로 정렬
    tmp = sorted(cnt.items(), key = lambda x:x[1], reverse=True)

    for a in tmp :
        key, value = a

        # 초기값 0과 비교해서 내림차순 정렬한 tmp를 순회하면서 비교
        if max_num < value :
            # key값들을 담는 list에 저장
            key_lst.append(key)
            # max_value는 더 큰값인 value로 바꿔준다.
            max_num = value

        # value값이 같다면
        # value에 대한 정보는 이미 max_num에 저장되어 있으니
        # key list에만 같은 value를 같는 key를 저장
        elif max_num == value :
            key_lst.append(key)

        else :
            break

    # 같은 value를 갖는 키들중 가장 큰값을 표시해준다.
    print("#{} {} {}".format(x+1, max(key_lst), max_num))

