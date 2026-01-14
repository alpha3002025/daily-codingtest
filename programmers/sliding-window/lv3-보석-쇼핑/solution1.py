from collections import defaultdict

def solution(gems):
    kind_count = len(set(gems))
    window_size = len(gems)
    
    ## [길이, 시작인덱스, 끝인덱스]
    window = [float('inf'), 0, 0]
    
    ## 현재 구간의 보석 개수 카운트 용도의 딕셔너리
    gem_dict = defaultdict(int)
    
    start,end = 0,0
    
    while True:
        ## 모든 보석을 모았을때 : 최솟값을 갱신하고, 윈도우를 줄여본다.(start 증가)
        if len(gem_dict) == kind_count:
            if (end - start) < window[0]:
                ## 참고) start +1 을 한 이유는 답 제출시 1 based index 로 제출 해야 해서...
                window = [end - start, start + 1, end] 
            
            ## start 포인터를 앞으로 이동 (이전 값 -1 + 오른쪽으로 이동)
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]] ## 개수가 0이면 키 삭제
            start += 1
        
        ## end 가 끝에 도달했을 때는 검사를 끝낸다.
        elif end == window_size:
            break
            
        ## 아직 모두 모은게 아니라면, 범위를 늘려본다.
        else:
            gem_dict[gems[end]] += 1
            end += 1
    
    return [window[1], window[2]]


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))