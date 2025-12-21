# 둘만의 암호

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/155652)

문자열 `s`의 각 문자를 `index`만큼 뒤의 알파벳으로 바꿉니다.
단, `skip` 문자열에 포함된 알파벳은 **세지 않고 건너뜁니다**.
- 예: s="a", skip="b", index=1 -> 'a' 다음은 'b'지만 건너뛰고 'c'가 됨.
- 'z' 다음은 'a'로 순환합니다.

## 해결 전략
알파벳 순환 로직에 "특정 문자 제외" 조건이 추가된 문제입니다.
가장 쉬운 방법은 **사용 가능한 알파벳 목록**을 미리 만들어두는 것입니다.

1. 모든 소문자 'a'~'z' 중에서 `skip`에 있는 문자를 뺍니다.
2. 남은 유효한 문자들로 구성된 새로운 리스트(또는 문자열)를 만듭니다.
3. 이 리스트에서 `s`의 각 문자의 현재 인덱스를 찾고, `+ index` 만큼 이동한 새 문자를 찾습니다.
    - 리스트 길이를 넘어가는 경우 모듈러 연산(`% len`)으로 순환 처리합니다.

### 알고리즘 순서
1. `valid_chars` = "abcdef...z"에서 `skip` 문자 제거.
    - 정렬된 상태 유지됨 (a부터 z 순서).
2. `result` 문자열 생성.
3. `s`의 각 문자 `c`에 대해:
    - `valid_chars`에서 `c`의 인덱스 `curr_idx` 찾기.
    - `new_idx = (curr_idx + index) % len(valid_chars)`
    - `result += valid_chars[new_idx]`
4. 반환.

## Python 코드

```python
def solution(s, skip, index):
    # 1. 사용 가능한 알파벳 리스트 생성 (skip 제외)
    # ascii code 97('a') ~ 122('z')
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    valid_chars = [char for char in alphabet if char not in skip]
    
    answer = []
    
    n = len(valid_chars)
    
    for char in s:
        # 현재 문자의 valid_chars 내 인덱스 찾기
        curr_idx = valid_chars.index(char)
        
        # index 만큼 뒤로 이동 (순환 고려)
        new_idx = (curr_idx + index) % n
        
        answer.append(valid_chars[new_idx])
        
    return "".join(answer)
```

## 배운 점 / 팁
- **필터링된 공간에서의 이동**: 제외해야 할 요소가 있을 때, 매번 검사하며 이동하는 것보다 **미리 유효한 요소들만 추려낸 리스트**를 만들고 그 안에서 인덱스 연산을 하는 것이 훨씬 간단하고 강력합니다.
- `string.ascii_lowercase`를 import해서 알파벳 목록을 얻을 수도 있습니다.
