def solution(n, info):
    max_diff = 0
    answer = []
    
    def dfs(idx, arrows, remain):
        nonlocal max_diff, answer
        
        if idx == 11 or remain == 0:
            # 남은 화살은 0점(idx 10)에 몰아줌
            if remain > 0:
                arrows[10] += remain
                
            # 점수 계산
            apeach_score = 0
            ryan_score = 0
            for i in range(11):
                if info[i] == 0 and arrows[i] == 0:
                    continue
                if info[i] >= arrows[i]:
                    apeach_score += (10 - i)
                else:
                    ryan_score += (10 - i)
            
            diff = ryan_score - apeach_score
            
            if diff > 0:
                if diff > max_diff:
                    max_diff = diff
                    answer = list(arrows)
                elif diff == max_diff:
                    # 낮은 점수를 더 많이 맞힌 경우 선택 (리스트 역순 비교시 더 큰 것이 답)
                    for i in range(10, -1, -1):
                        if arrows[i] > answer[i]:
                            answer = list(arrows)
                            break
                        elif arrows[i] < answer[i]:
                            break
            
            # 화살 회수 (Backtracking) - 0점 몰아준거 취소
            if remain > 0:
                arrows[10] -= remain
            return

        # 1. 현재 점수(10-idx)를 먹는 경우 (어피치보다 1발 더 쏨)
        needed = info[idx] + 1
        if remain >= needed:
            arrows[idx] = needed
            dfs(idx + 1, arrows, remain - needed)
            arrows[idx] = 0 # 복구
            
        # 2. 현재 점수를 포기하는 경우 (0발 쏨)
        dfs(idx + 1, arrows, remain)

    dfs(0, [0]*11, n)
    
    if max_diff == 0:
        return [-1]
        
    return answer


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))