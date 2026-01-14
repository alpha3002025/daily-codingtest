from collections import defaultdict

def solution(gems):
    kinds = len(set(gems))
    n = len(gems)
    
    answer = [1, n] # 일단 전체 구간으로 초기화
    min_len = n
    
    gem_dict = defaultdict(int)
    
    start = 0
    end = 0
    
    # 슬라이딩 윈도우
    # end가 n보다 작을 때까지, 혹은 start가 end보다 작거나 같을 때까지
    
    while True:
        # 모든 종류가 다 모였으면 -> start를 줄여서 최소 찾기
        if len(gem_dict) == kinds:
            current_len = end - start
            if current_len < min_len:
                min_len = current_len
                answer = [start + 1, end] # end는 이미 증가되어 있는 상태가 아니라, 현재 포함된 마지막 인덱스를 가리켜야 함?
                                         # 로직을: gems[end] 추가 -> check -> start 이동 방식이면 end는 현재 마지막 위치
            
            # start 이동 (축소)
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
            
        elif end == n:
            break
            
        else:
            # 아직 부족하면 -> end 늘리기
            gem_dict[gems[end]] += 1
            end += 1
            
    return answer