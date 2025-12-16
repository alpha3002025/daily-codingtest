
def time_to_seconds(t):
    m, s = map(int, t.split(':'))
    return m * 60 + s

def seconds_to_time(s):
    m = s // 60
    s = s % 60
    return f"{m:02d}:{s:02d}"

def solution(video_len, pos, op_start, op_end, commands):
    total_len = time_to_seconds(video_len)
    current = time_to_seconds(pos)
    op_s = time_to_seconds(op_start)
    op_e = time_to_seconds(op_end)
    
    # 1. 오프닝 구간 체크 (명령 수행 전)
    if op_s <= current <= op_e:
        current = op_e
        
    for cmd in commands:
        if cmd == "prev":
            current = max(0, current - 10)
        elif cmd == "next":
            current = min(total_len, current + 10)
            
        # 2. 오프닝 구간 체크 (명령 수행 후)
        # 문제의 조건: "현재 재생 위치가 오프닝 구간인 경우 자동으로 오프닝이 끝나는 위치로 이동합니다."
        # 이는 이동 직후에도 적용되어야 함.
        if op_s <= current <= op_e:
            current = op_e
            
    return seconds_to_time(current)

if __name__ == "__main__":
    # Test case 1
    # 입출력 예 #1
    # video_len="34:33", pos="13:00", op_start="00:55", op_end="02:55", commands=["next", "prev"]
    # 13:00 -> next -> 13:10. Not in opening.
    # 13:10 -> prev -> 13:00. Not in opening.
    # Result: 13:00
    print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])) # Expected: "13:00"

    # Test case 2
    # 입출력 예 #2
    # video_len="10:55", pos="00:05", op_start="00:15", op_end="06:55", commands=["prev", "next", "next"]
    # 00:05 -> Initial Check (Not in 00:15~06:55)
    # prev -> 00:00 -> Check (Not in opening)
    # next -> 00:10 -> Check (Not in opening)
    # next -> 00:20 -> Check (In 00:15~06:55) -> Jump to 06:55
    print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"])) # Expected: "06:55"

    # Test case 3
    # 입출력 예 #3
    # video_len="07:22", pos="04:05", op_start="00:15", op_end="04:07", commands=["next"]
    # 04:05 -> Initial Check (In 00:15~04:07) -> Jump to 04:07
    # next -> 04:17 -> Check (Not in opening)
    print(solution("07:22", "04:05", "00:15", "04:07", ["next"])) # Expected: "04:17"
