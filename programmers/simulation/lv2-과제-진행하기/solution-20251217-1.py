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
        else:
            stack.append((name, playtime - time_gap))
    
    ## 마지막 과제는 무조건 완료
    answer.append(parsed_plans[-1][0])
    
    ## 남은 과제들은 역순으로 완료
    while stack:
        answer.append(stack.pop()[0])
    
    return answer