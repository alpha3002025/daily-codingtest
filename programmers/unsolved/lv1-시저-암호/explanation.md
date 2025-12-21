# 시저 암호

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12926)

문자열 `s`의 각 문자를 `n`만큼 민 시저 암호를 만드세요.
- 공백은 밀지 않습니다.
- 'z' 다음은 'a', 'Z' 다음은 'A'입니다.

## 해결 전략
아스키 코드(`ord`, `chr`)를 사용합니다.
- 대문자(65~90), 소문자(97~122) 범위를 유지하며 순환해야 합니다.
- `(ord(char) - base + n) % 26 + base` 공식을 사용합니다.

### 알고리즘 순서
1. `answer` = ""
2. `s` 순회 (`char`):
    - 공백이면 그대로 추가.
    - 대문자면 `base = 65` (ord('A'))
    - 소문자면 `base = 97` (ord('a'))
    - 변환된 문자 = `chr((ord(char) - base + n) % 26 + base)`
    - 추가.
3. 반환.

## Python 코드

```python
def solution(s, n):
    result = []
    
    for char in s:
        if char == " ":
            result.append(" ")
            continue
            
        if char.isupper(): # 대문자
            base = ord('A')
        else: # 소문자
            base = ord('a')
            
        # 0~25 범위로 변환 -> n 더하기 -> 모듈러 26 -> 다시 문자로
        shifted = (ord(char) - base + n) % 26 + base
        result.append(chr(shifted))
        
    return "".join(result)
```

## 배운 점 / 팁
- **순환 이동**: 알파벳 같은 유한 집합의 순환은 `(0-indexed값 + 이동) % 길이`로 처리하는 것이 정석입니다.
