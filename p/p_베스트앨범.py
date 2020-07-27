'''from collections import defaultdict

def counter() :
    i = 0
    while True:
        yield i
        i += 1

def solution(genres, plays):
    play_coount_by_genre = defaultdict(int)
    songs_in_genre = defaultdict(list)

    for song_id, genre, play in zip(counter(), genres, plays) :
        play_coount_by_genre[genre] += play
        songs_in_genre[genre].append((-play, song_id))

    genre_in_order = sorted(play_coount_by_genre.keys(), key = lambda g : play_coount_by_genre[g], reverse=True)

    answer = list()
    for genre in genre_in_order :
        print(genre)
        answer.extend([song_id for minus_play, song_id in sorted(songs_in_genre[genre])[:2]])
    return answer'''


def solution(genres, plays):
    dic = {}
    for idx, genre in enumerate(genres):
        if genre in dic.keys():   # 기존에 dic의 키값에 있는 장르면 여기의 if문을 탐색
            temp = dic[genre]
            temp['sum'] += plays[idx]           # sum은 장르마다 누적 재생 횟수에 따라 우선순위가 달라지기 때문에
            temp['plays'][idx] = plays[idx]     # plays.... 그냥 단순히 play횟수들을 저장해준다. temp를 사용해서 먼저
        else:       # 없다면 새로 넣어야 할테니 key값을 genre로 하고 value값을 새로운 딕셔너리로 해서 sum과 plays로...
            dic[genre] = {'sum':plays[idx], 'plays':{idx : plays[idx]}}

    result = []
    for k, v in sorted(dic.items(), key=lambda dic: dic[1]['sum'],reverse=True):   # 누적 재생횟수가 많은 장르 먼저 탐색
        plays_dic = v['plays']          # plays를 키값으로 갖는 value dict형태 = 재생횟수들이 담긴 idx(고유인덱스) : plays(재생횟수)
        for idx, plays in sorted(plays_dic.items(), key=lambda plays_dic: plays_dic[1], reverse=True)[:2]:
            # 그 plays_dic을 받아와서 다시 items중에서 value값으로 정렬을 하고 갯수는 앞에서 두개만.. = 상위값 두개를 뽑아오는거니까
            # 그리고 그 인덱스의 값만 result에 append시켜주고
            # 그럼 예제의 순서대로라면 pop에서 가장 많이 들은 두개 노래의 idx를 넣어주고 그 다음에는
            # classic의 idx를 넣어주는 코드..
            result.append(idx)

    return result
## 나중에 반드시 복습


if __name__ == '__main__':
    genres, plays = ['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]

    print(solution(genres, plays))