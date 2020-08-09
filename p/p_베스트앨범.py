# 장르 별로 가장 많이 재생된 노래를 두개씩 모아 베스트 앨범을 출시
# 노래는 고유번호로 구분
# 수록 기준
# 1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
# 2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
# 3. 장르 내에서 재생 횟수가 같은 노래 중에서 고유 번호가 낮은 노래를 먼저 수록
def solution(genres, plays):
    answer = []
    tmp_dict = {}
    # 장르와 재생횟수를 리스트로 묶는다.
    tmp_lst = list(zip(genres, plays))

    # 고유 번호 : (장르, 플레이 횟수)로 새로운 딕셔너리 생성
    for idx, values in enumerate(tmp_lst):
        tmp_dict[idx] = values

    # 장르별 재생 횟수
    genre_play = {}
    for gen, pla in tmp_lst:
        if gen not in genre_play.keys() :
            genre_play[gen] = pla
        else:
            tmp_num = genre_play[gen]
            genre_play[gen] = tmp_num+pla

    # print("장르가 수록 되어야 하는 순서 : ", end='')
    ord_lst = []
    for key, value in sorted(genre_play.items(), key=lambda x : x[1], reverse=True):
        ord_lst.append(key)

    # 전체 dict에서 특정 장르만 따로 빼온다?
    # 장르 : (고유 id, 재생횟수) 딕셔너리 생성
    genre_dict = {}
    for idx, (gen, play) in tmp_dict.items():
        if gen not in genre_dict.keys():
            genre_dict[gen] = [(idx, play)]

        else :
            tmp = genre_dict[gen]
            tmp = tmp.append((idx, play))

    # 장르마다 많이 재생된 노래 두 곡씩...
    # print('-'*20)
    # print(sorted(genre_dict[ord_lst[1]], key=lambda x : x[1], reverse=True))

    for gen in ord_lst:
        check_lst = genre_dict[gen]
        check_lst = sorted(check_lst, key=lambda x : x[1], reverse=True)
        for i in range(2):
            try :
                answer.append(check_lst[i][0])
            except:  # 장르에 수록된 곡이 1개일 경우 try except문을 사용하지 않으면 런타임 에러 발생
                pass   # 아무런 작동을 안하고 그냥 넘어가도록 한다.
    return answer

if __name__ == '__main__':
    genres, plays = ['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]

    print(solution(genres, plays))


# def solution(genres, plays):
#     dic = {}
#     for idx, genre in enumerate(genres):
#         if genre in dic.keys():   # 기존에 dic의 키값에 있는 장르면 여기의 if문을 탐색
#             temp = dic[genre]
#             temp['sum'] += plays[idx]           # sum은 장르마다 누적 재생 횟수에 따라 우선순위가 달라지기 때문에
#             temp['plays'][idx] = plays[idx]     # plays.... 그냥 단순히 play횟수들을 저장해준다. temp를 사용해서 먼저
#         else:       # 없다면 새로 넣어야 할테니 key값을 genre로 하고 value값을 새로운 딕셔너리로 해서 sum과 plays로...
#             dic[genre] = {'sum':plays[idx], 'plays':{idx : plays[idx]}}
#
#     result = []
#     for k, v in sorted(dic.items(), key=lambda dic: dic[1]['sum'],reverse=True):   # 누적 재생횟수가 많은 장르 먼저 탐색
#         plays_dic = v['plays']          # plays를 키값으로 갖는 value dict형태 = 재생횟수들이 담긴 idx(고유인덱스) : plays(재생횟수)
#         for idx, plays in sorted(plays_dic.items(), key=lambda plays_dic: plays_dic[1], reverse=True)[:2]:
#             # 그 plays_dic을 받아와서 다시 items중에서 value값으로 정렬을 하고 갯수는 앞에서 두개만.. = 상위값 두개를 뽑아오는거니까
#             # 그리고 그 인덱스의 값만 result에 append시켜주고
#             # 그럼 예제의 순서대로라면 pop에서 가장 많이 들은 두개 노래의 idx를 넣어주고 그 다음에는
#             # classic의 idx를 넣어주는 코드..
#             result.append(idx)
#
#     return result