# https://programmers.co.kr/learn/courses/30/lessons/77484?language=python3

def solution(lottos, win_nums):

    zoker = lottos.count(0)
    
    win_counter = 0
    for win_num in win_nums:
        if win_num in lottos:
            win_counter += 1
    
    return [7-win_counter-zoker if 7-win_counter-zoker<= 6 else 6, 7-win_counter if 7-win_counter <= 6 else 6]

if __name__ == '__main__':
    
    input_data =[
        ([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]),
        ([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]),
        ([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
    ]
    for lottos, win_nums in input_data:
        print(solution(lottos, win_nums))
        print()
    