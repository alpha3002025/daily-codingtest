import re

def solution(dartResult):
    # 1. 정규표현식 컴파일
    # 그룹 1: 점수 (0~10)
    # 그룹 2: 보너스 (S, D, T)
    # 그룹 3: 옵션 (*, #, 또는 빈 문자열)
    pattern = re.compile(r'(\d+)([SDT])([*#]?)')
    
    # findall은 매칭되는 모든 패턴을 튜플의 리스트로 반환합니다.
    # 예: [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]
    matches = pattern.findall(dartResult)
    
    scores = []
    
    for idx, (score_str, bonus, option) in enumerate(matches):
        score = int(score_str)
        
        # 보너스 계산
        if bonus == 'S':
            score = score ** 1
        elif bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
            
        # 옵션 계산
        if option == '*':
            score *= 2 # 현재 점수 2배
            if idx > 0: # 첫 번째 기회가 아니라면
                scores[idx-1] *= 2 # 이전 점수도 2배
        elif option == '#':
            score *= -1 # 현재 점수 마이너스
            
        scores.append(score)
        
    return sum(scores)