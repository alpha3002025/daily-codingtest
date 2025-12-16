
def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    def get_count(t):
        # 분침과 초침이 겹치는 횟수 계산
        # 초침속도 - 분침속도 = 5.9 deg/s = 59/10 deg/s
        # 겹치는 주기: 360 / (59/10) = 3600 / 59 초
        # t초 동안 겹치는 횟수 = t / (3600/59) = t * 59 / 3600
        cnt_m = (t * 59) // 3600
        
        # 시침과 초침이 겹치는 횟수 계산
        # 초침속도 - 시침속도 = 6 - 1/120 = 719/120 deg/s
        # 겹치는 주기: 360 / (719/120) = 43200 / 719 초
        # t초 동안 겹치는 횟수 = t * 719 / 43200
        cnt_h = (t * 719) // 43200
        
        # 12시 0분 0초 (43200초)에는 시침, 분침, 초침이 모두 겹침
        # 이 경우 위의 두 계산에서 각각 카운트되므로 중복 제거 필요
        if t >= 43200:
            return cnt_m + cnt_h - 1
        
        return cnt_m + cnt_h

    def is_alarm(t):
        # 해당 시각(t초)에 알람이 울리는지 확인
        # 1. 분침과 초침 일치 여부
        if (t * 59) % 3600 == 0:
            return True
        # 2. 시침과 초침 일치 여부
        if (t * 719) % 43200 == 0:
            return True
        return False

    ans = get_count(end) - get_count(start)
    if is_alarm(start):
        ans += 1
        
    return ans

if __name__ == '__main__':
    # 입출력 예시 테스트
    print(solution(0, 5, 30, 0, 7, 0)) # Expected: 2
    print(solution(12, 0, 0, 12, 0, 30)) # Expected: 1
    print(solution(0, 6, 1, 0, 6, 6)) # Expected: 0
    print(solution(11, 59, 30, 11, 59, 59)) # Expected: 1
    print(solution(11, 58, 59, 11, 59, 0)) # Expected: 1
    print(solution(1, 5, 5, 1, 5, 6)) # Expected: 2
    print(solution(0, 0, 0, 23, 59, 59)) # Expected: 2852
