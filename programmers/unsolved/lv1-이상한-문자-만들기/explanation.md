# 이상한 문자 만들기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12930)

문자열 `s`의 **각 단어별로** 짝수 인덱스는 대문자, 홀수 인덱스는 소문자로 바꿉니다.
- 단어는 공백 하나 이상으로 구분됩니다.
- 전체 인덱스가 아니라, **단어별 인덱스** 기준입니다.

## 해결 전략
공백을 기준으로 자르면(`split()`), 연속된 공백 정보가 사라질 수 있습니다(예: "  hello  " -> `['', '', 'hello', '', '']`가 아니라 `['hello']`만 남을 수도 있음).
따라서 문자열을 처음부터 끝까지 순회하며, 공백을 만나면 인덱스를 초기화하는 방식으로 접근하거나, `split(' ')`을 사용하여 공백을 보존해야 합니다.

### 알고리즘 순서
1. `words` = `s.split(" ")` (separator 지정 필수! 그냥 `split()`은 연속 공백 무시)
2. `result` = []
3. 각 `word`에 대해:
    - 변환된 단어 `new_word` 생성.
    - `for i, char`: 
        - 짝수면 `upper`, 홀수면 `lower`
    - `result.append(new_word)`
4. return `" ".join(result)`

## Python 코드

```python
def solution(s):
    # 공백이 여러 개일 수 있으므로 split(' ') 사용 (그냥 split()은 안됨)
    words = s.split(" ")
    
    new_words = []
    
    for word in words:
        converted = ""
        for i, char in enumerate(word):
            if i % 2 == 0:
                converted += char.upper()
            else:
                converted += char.lower()
        new_words.append(converted)
        
    # 원래 공백 유지하며 결합
    return " ".join(new_words)
```

## 배운 점 / 팁
- **split() vs split(" ")**: 이 문제의 핵심 함정입니다. `split()`은 모든 공백(탭, 줄바꿈 포함)을 묶어서 처리하지만, `split(" ")`은 공백 하나하나를 구분자로 봅니다. 문제에서 "하나 이상의 공백"이라고 했고 원본 형태를 유지해야 하므로 후자가 필수입니다.
