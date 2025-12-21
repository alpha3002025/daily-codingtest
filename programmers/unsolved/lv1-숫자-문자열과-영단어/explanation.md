# 숫자 문자열과 영단어

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/81301)

숫자의 일부가 영단어로 바뀐 문자열 `s`가 주어집니다. (예: "one4seveneight")
이를 원래 숫자(`1478`)로 바꿔서 반환하세요.
- "zero" ~ "nine" -> 0 ~ 9

## 해결 전략
문자열 치환(`replace`) 문제입니다.
영단어와 숫자의 매핑 테이블을 만들어두고 하나씩 바꾸면 됩니다.

### 알고리즘 순서
1. `words` = `["zero", "one", ..., "nine"]`
2. `i` from 0 to 9:
    - `s` = `s.replace(words[i], str(i))`
3. return `int(s)`

## Python 코드

```python
def solution(s):
    english_nums = [
        "zero", "one", "two", "three", "four", 
        "five", "six", "seven", "eight", "nine"
    ]
    
    for i, word in enumerate(english_nums):
        # 해당 영단어가 있으면 숫자로 치환
        s = s.replace(word, str(i))
        
    return int(s)
```

## 배운 점 / 팁
- **Enumrate & Replace**: 인덱스(`i`)와 값(`word`)을 동시에 활용하여 간단하게 치환할 수 있습니다.
