# [3차] 압축

## 문제 설명
LZW(Lempel-Ziv-Welch) 압축 알고리즘을 구현하는 문제입니다.
1. 길이가 1인 모든 단어를 사전에 등록 (A~Z, 인덱스 1~26).
2. 현재 입력에서 사전에 있는 가장 긴 문자열 `w`를 찾음.
3. `w`의 인덱스를 출력.
4. 입력에서 `w`를 제거.
5. 입력에 다음 글자 `c`가 남아있다면, `w+c`를 사전에 등록(새 인덱스 부여).
6. 반복.

### 핵심 개념
1.  **사전 (Dictionary)**: `{단어: 인덱스}` 매핑을 관리합니다.
2.  **가장 긴 일치 찾기 (Greedy Match)**:
    - 현재 위치에서 한 글자씩 늘려가며 사전에 있는지 확인합니다.
    - 더 이상 사전에 없는 문자열이 나오면, 직전까지의 문자열이 `w`입니다.

## Python 풀이

```python
def solution(msg):
    # 1. 초기 사전 생성 (A~Z)
    # chr(65) = 'A'
    dictionary = {chr(65 + i): i + 1 for i in range(26)}
    
    answer = []
    w = ""
    idx = 0
    next_code = 27
    
    # 메시지 전체 순회
    # while 루프와 인덱싱을 쓰는 것이 문자열 조작보다 빠름
    i = 0
    while i < len(msg):
        # 현재 글자부터 시작해서 사전에 있는 가장 긴 단어 찾기
        w = msg[i]
        
        # w 다음 글자를 계속 붙여보며 확인
        length = 1
        while i + length < len(msg) and (msg[i : i + length + 1] in dictionary):
            length += 1
            w = msg[i : i + length]
            
        # w는 사전에 있는 가장 긴 단어
        answer.append(dictionary[w])
        
        # w + c (다음 글자)를 사전에 등록
        if i + length < len(msg):
            c = msg[i + length]
            dictionary[w + c] = next_code
            next_code += 1
            
        # 처리한만큼 인덱스 이동
        i += length
        
    return answer
```

### 코드 설명
- `dictionary`: 초기에는 A(1)부터 Z(26)까지 저장됩니다.
- 내부 `while`: 현재 위치(i)에서 시작하는 부분 문자열이 사전에 있는 동안 계속 길이를 늘립니다.
- 사전에 없는 단어(`w+c`)를 만나면 `w`의 인덱스를 출력하고 `w+c`를 사전에 추가합니다.
- 시간 복잡도: 문자열 길이 $N$에 대해, 내부 루프에서 최대 $L$(단어 최대 길이)만큼 돕니다. 전체적으로 $O(N \times L)$입니다.
