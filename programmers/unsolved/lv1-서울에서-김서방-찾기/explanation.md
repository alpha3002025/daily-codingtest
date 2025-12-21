# 서울에서 김서방 찾기

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12919)

문자열 배열 `seoul`에서 "Kim"의 위치(인덱스)를 찾아 "김서방은 x에 있다"를 반환하세요.

## 해결 전략
리스트의 `index` 메소드를 사용합니다.

### 알고리즘 순서
1. `idx` = `seoul.index("Kim")`
2. return `f"김서방은 {idx}에 있다"`

## Python 코드

```python
def solution(seoul):
    idx = seoul.index("Kim")
    return f"김서방은 {idx}에 있다"
```

## 배운 점 / 팁
- **f-string**: 문자열 포매팅의 표준입니다.
