from collections import Counter

def solution(clothes):
    answer = 1

    tmp_lst=[]
    for check in clothes:
        tmp_lst.append(check[1])
    check_dict = Counter(tmp_lst)
    # check_dict = Counter([a for _, a in clothes])

    for val in check_dict.values():
        answer *= (val+1)

    return answer-1

if __name__ == '__main__':
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    # clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

    print(solution(clothes))