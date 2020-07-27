sugar = int(input())
number_of_package = 0

while sugar > 0:
    # 5의 배수가 아닐 경우
    if sugar % 5 != 0:
        sugar -= 3
        if sugar < 0:           # 3을 뺐을때 음수가 된다면?
            number_of_package = -1    # -1 출력
            break                     # whille문 탈출
        number_of_package += 1  # 3을 뺐을때 양수일 경우
    # 5의 배수일 경우
    elif sugar % 5 == 0:
        number_of_package += 1  # 설탕 봉지 개수 한개 추가하고
        sugar -= 5   # 5를 빼준다
    # 5의 배수도 아니고 3의 배수도 아닐 경우  (-1 출력)
    elif sugar % 5 != 0 and sugar % 3 != 0:
        number_of_package = -1

print(number_of_package)

# 출처 : https://this-programmer.com/entry/%EB%B0%B1%EC%A4%802839%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%84%A4%ED%83%95-%EB%B0%B0%EB%8B%AC