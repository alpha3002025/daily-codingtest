def solution(n,a,b):
    round_count = 0
    
    while a != b:
        a = (a+1) // 2 ## a 가 속한 게임의 다음 게임 매칭
        b = (b+1) // 2 ## b 가 속한 게임의 다음 게임 매칭
        round_count += 1
    
    return round_count

print(solution(8,4,7))