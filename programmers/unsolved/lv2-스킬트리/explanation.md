# 스킬트리

## 문제 설명
선행 스킬 순서 `skill` (예: "CBD")가 주어질 때, 유저들의 스킬 트리 `skill_trees` 중 올바른 순서로 배운 것이 몇 개인지 찾습니다. 선행 스킬에 포함되지 않은 스킬은 아무 때나 배워도 됩니다.
순서: C -> B -> D. (B를 배우려면 C를 먼저 배워야 함)

### 핵심 개념
1.  **필터링 (Filtering)**: 유저의 스킬 트리에서 `skill`에 포함되지 않은 문자들은 순서에 영향을 주지 않으므로 제거합니다.
2.  **접두사 확인 (Prefix Check)**: 필터링된 문자열이 `skill`의 **앞부분(Prefix)**과 일치하는지 확인합니다.
    - 예: `skill`="CBD"
    - "BACDE" -> "BCD" (X, B가 C보다 먼저 옴)
    - "CBADF" -> "CBD" (O)
    - "AECB" -> "CB" (O)
    - "BDA" -> "BD" (X)
    - 남은 문자열이 "C", "CB", "CBD" 중 하나여야 합니다.

## Python 풀이

```python
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
```


### 코드 설명
- `[c for c in tree if c in skill]` : 리스트 컴프리헨션으로 선행 조건이 있는 스킬만 추출합니다.
- `skill.startswith(filtered_skill)` : 추출된 스킬 순서가 정해진 순서의 앞부분과 일치하는지 봅니다.
    - `skill="CBD"` 일 때, `filtered="CB"`는 True (C 배우고 B 배움).
    - `filtered="BD"`는 False (C 없이 B 배움).
    - `filtered=""`는 True (아무것도 선행 스킬을 안 배움 -> 가능).


## 참고 문법: `startswith`
- **`str.startswith(prefix)`**: 문자열이 특정 접두사(`prefix`)로 시작하는지 (`True`/`False`) 확인합니다.
- **특징**:
  - 대소문자를 구분합니다.
  - 인자로 **튜플**을 넘기면 여러 접두사 중 하나라도 일치하면 `True`를 반환합니다.
- **예시**:
```python
s = "Hello World"
print(s.startswith("He"))      # True
print(s.startswith("world"))   # False
print(s.startswith(("Hi", "He"))) # True (Hi 또는 He로 시작하는가?)
```


## 나의 풀이
### 2025/12/19 (1)
```python
def solution(skill, skill_trees):
    count = 0
    for curr_skill in skill_trees:
        found_skills = "".join([c for c in curr_skill if c in skill])
        
        ## found_skills 가 skill 보다 더 작은 문자열일 수 있다.
        if skill.startswith(found_skills):
            count += 1
        
    return count
```