# 2016년

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/12901)

2016년 `a`월 `b`일은 무슨 요일일까요?
- 2016년 1월 1일은 금요일입니다.
- 2016년은 윤년입니다 (2월 29일까지 있음).
- 요일: SUN, MON, TUE, WED, THU, FRI, SAT.

## 해결 전략
1월 1일부터 a월 b일까지 총 흐른 날짜(`total_days`)를 구한 뒤, 7로 나눈 나머지를 이용합니다.
1. 각 월의 일수 배열: `[31, 29, 31, 30, ...]`
2. `total` 합산 (+ b일 - 1)
3. `days[(total + 5) % 7]` (금요일 시작이므로 offset 5)
    - 또는 요일 배열을 `[FRI, SAT, SUN ...]`로 정의하면 `total % 7`로 바로 접근 가능.

### 알고리즘 순서
1. `months` = `[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]`
2. `days` = `["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]` (금요일이 0번 인덱스)
3. `total` = `sum(months[:a])` + `b` - 1
4. return `days[total % 7]`

## Python 코드

```python
def solution(a, b):
    # 2016년 각 월의 일수 (윤년이므로 2월은 29일)
    month_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 1월 1일이 금요일이므로 금요일부터 시작하는 배열 생성
    weekdays = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    
    # 1월 1일부터 a월 b일까지 총 일수 계산
    # a월 이전 달들의 일수 합 + b일 - 1 (1월 1일 포함하기 위해 -1)
    total_days = sum(month_days[:a]) + b - 1
    
    return weekdays[total_days % 7]
```

## 배운 점 / 팁
- **날짜 계산**: 라이브러리(`datetime`)를 써도 되지만, 코딩테스트에서는 직접 계산하는 로직을 요구할 때가 많습니다. 윤년 체크와 기준일(Offset) 설정이 핵심입니다.
