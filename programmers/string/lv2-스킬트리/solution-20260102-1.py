def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        # 1. skill에 있는 문자만 남기기
        filtered_skill = "".join([c for c in tree if c in skill])
        
        # 2. 남은 문자열이 skill의 접두사인지 확인
        # skill이 "CBD"일 때, filtered가 "C", "CB", "CBD", ""(빈문자열) 이면 가능
        if skill.startswith(filtered_skill):
            answer += 1
            
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))