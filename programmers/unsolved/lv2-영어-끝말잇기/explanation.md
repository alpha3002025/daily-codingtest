# 영어 끝말잇기
prev, curr 을 이용한 비교를 사용하는 전형적인 문제<br/>
<br/>

## 문제 설명
`n`명이 돌아가면서 영어 끝말잇기를 합니다. 탈락하는 사람의 번호와 몇 번째 차례인지 구하세요.
탈락 조건:
1. 앞사람이 말한 단어의 마지막 문자로 시작하지 않는 경우.
2. 이전에 등장했던 단어를 말한 경우.
3. 한 글자 단어를 말한 경우 (문제 조건엔 없지만 보통 미포어함, 여기선 2번 조건이 메인).

### 핵심 개념
1.  **순회 (Loop)**: 단어 리스트를 인덱스 `i`로 순회합니다.
    - 사람 번호: `(i % n) + 1`
    - 차례: `(i // n) + 1`
2.  **검증 (Validation)**:
    - 중복 검사: `curr_word in used_words` (`set` 활용)
    - 끝말잇기 규칙: `prev_word[-1] != curr_word[0]`

<br/>

## 개념 설명 코드
```python
def solution(n, words):
    answer = []
    
    prev = words[0]
    used = set([prev])
    
    for i in range(1, len(words)):
        curr = words[i]
        
        if not (curr[0] == prev[-1] and curr not in used):
            fail_person = (i % n) + 1
            fail_round = (i // n) + 1
            return [fail_person, fail_round]
        
        prev = curr
        used.add(curr)
    
    return [0,0]
```

<br/>

## Python 풀이

```python
def solution(n, words):
    used = set()
    used.add(words[0])
    
    # 두 번째 단어부터 확인
    for i in range(1, len(words)):
        curr = words[i]
        prev = words[i-1]
        
        # 탈락 조건 확인
        # 1. 이전 단어의 끝 글자와 현재 단어의 앞 글자가 다름
        # 2. 이미 사용된 단어임
        if prev[-1] != curr[0] or curr in used:
            # 탈락자 번호, 차례 계산
            number = (i % n) + 1
            order = (i // n) + 1
            return [number, order]
        
        used.add(curr)
        
    return [0, 0]
```

### 코드 설명
- 첫 번째 단어는 무조건 통과이므로 `used`에 넣고 루프를 인덱스 1부터 시작합니다.
- `i`번째 단어(0-based)를 말한 사람은 `i % n + 1`번째 사람입니다.
- $N$이 작고 단어 길이도 짧아 $O(N)$으로 충분합니다.
