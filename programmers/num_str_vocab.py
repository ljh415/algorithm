def solution(s):    
    convert_map = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "zero" : 0
    }
    
    for str_num in convert_map:
        s = s.replace(str_num, str(convert_map[str_num]))
    
    return int(s)

if __name__ == '__main__':
    input_args =[
        "one4seveneight", "23four5six7", "2three45sixseven", "123"
    ]
    for s in input_args:
        print(solution(s))