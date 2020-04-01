from collections import Counter

def solution(clothes):
    answer = 1

    cou = Counter([a for _, a in clothes])

    for a in cou.values() :
        answer *= (a+1)

    return answer-1

if __name__ == "__main__" :
    clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
    # clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

    print(solution(clothes))
