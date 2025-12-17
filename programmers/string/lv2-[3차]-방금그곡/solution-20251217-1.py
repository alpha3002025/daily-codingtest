def replace_sharp(s):
    return s.replace('C#', 'c').replace('D#', 'd').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#', 'b').replace('E#','e')

def to_minutes(time_str):
    h, m = map(int, time_str.split(":"))
    return h*60 + m

def solution(m, musicinfos):
    # before = m
    m = replace_sharp(m)
    # print(f"before = {before}, after = {m}")
    
    answer = "(None)"
    max_play_time = -1
    
    for info in musicinfos:
        start,end,title,sheet = info.split(',')
        play_time = to_minutes(end) - to_minutes(start)
        sheet = replace_sharp(sheet)
        
        sheet_len = len(sheet)
        if play_time >= sheet_len: 
            ## 반복을 해서 붙여야 뒤로 돌아갔다가 앞으로 오는 구조를 찾을 수 있다.
            ## sheet 의 길이에 따라 play_time 내에서 반복을 하고, 남는 부분은 나머지 만큼 덧붙인다.
            full_sheet = sheet * (play_time // sheet_len) + sheet[:play_time % sheet_len]
        else:
            ## play_time 에 딱 맞거나, play_time 이 더 작으면 그 만큼 자른다.
            full_sheet = sheet[:play_time]
        
        if m in full_sheet:
            ## 재생된 시간이 제일 긴 음악 제목 + 재생시간 같을 경우 먼저 입력된 음악 제목 반환을 위한 조건
            if play_time > max_play_time:
                max_play_time = play_time
                answer = title
    
    return answer