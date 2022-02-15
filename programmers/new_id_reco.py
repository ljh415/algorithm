# https://programmers.co.kr/learn/courses/30/lessons/72410?language=python3
import re

def solution(new_id):

    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*()=+\[\{\]\}:?,<>/]','', new_id)    
    new_id = re.sub('\.+','.', new_id)
    if len(new_id)!=0:
        if new_id[0] == '.':
            new_id=new_id[1:]
    if len(new_id)!=0:
        if new_id[-1] == '.':
            new_id=new_id[:-1]
    if len(new_id) == 0:
        new_id += 'a'
    if len(new_id) >= 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id=new_id[:14]
    while len(new_id) < 3:
        new_id += new_id[-1]
    
    return new_id
    
if __name__ == '__main__':
    input_data =[
        "...!@BaT#*..y.abcdefghijklm",
        "z-+.^.",
        "=.=",
        "123_.def",
        "abcdefghijklmn.p"
    ]
    
    for data in input_data:
        print(solution(data))
        print()