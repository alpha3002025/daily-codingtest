def to_minutes(time):
    h,m = map(int, time.split(":"))
    return h*60 + m

def solution(plans):
    parsed_plans = []
    for name, start, playtime in plans:
        parsed_plans.append([name, to_minutes(start), int(playtime)])
    
    ## 시작 시간 빠른 순으로 정렬
    parsed_plans.sort(key=lambda x:x[1])
    
    # 멈춘 과제들
    stack = []
    answer = []
    
    for i in range(len(parsed_plans)-1):
        name, start_time, playtime = parsed_plans[i]
        next_start = parsed_plans[i+1][1]
        
        time_gap = next_start - start_time
        
        if playtime <= time_gap:
            answer.append(name) ## 현재 과제 완료
            remain_gap = time_gap - playtime
            
            ## 남은 시간 동안 멈춘 과제 수행
            while remain_gap > 0 and stack:
                prev_name, prev_remain = stack.pop()
                if prev_remain <= remain_gap: ## 이전 과제가 남은 시간 동안 끝낼수 있다면
                    answer.append(prev_name)
                    remain_gap -= prev_remain
                else: ## 이전 과제가 남은시간 보다 더 오랫동안 일 경우
                    ## 멈춘과제 일부 수행 후 다시 스텍에 push
                    stack.append((prev_name, prev_remain - remain_gap))
                    remain_gap = 0
        else: ## 다음 작업 시각이 현재 작업이 끝나기 전에 시작할 경우 멈춰두고 stack 에 (작업명, 남은시각)을 넣어둔다.
            stack.append((name, playtime - time_gap)) ## (현재작업명, 현재 작업의 남은 작업시간)을 stack 에 넣어둔다.
    
    ## 마지막 과제는 무조건 완료
    answer.append(parsed_plans[-1][0])
    
    ## 남은 과제들은 역순으로 완료
    while stack:
        answer.append(stack.pop()[0])
    
    return answer


print(solution(["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]))
print(solution(["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]))
print(solution(["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]))