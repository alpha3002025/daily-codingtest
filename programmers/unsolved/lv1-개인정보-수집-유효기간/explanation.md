# 개인정보 수집 유효기간

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/150370)

개인정보 수집 일자(`privacies`)와 약관 종류별 유효기간(`terms`)이 주어집니다.
오늘 날짜(`today`)를 기준으로 **유효기간이 지난(파기해야 할)** 개인정보들의 번호를 구하세요.
- 모든 달은 **28일**까지 있다고 가정합니다.
- 날짜 형식: "YYYY.MM.DD"

## 해결 전략
날짜 계산 문제입니다. 모든 달이 28일로 고정되어 있다는 점이 핵심입니다.
연/월/일을 따로 계산하면 올림/내림 처리가 복잡해질 수 있으므로, **모든 날짜를 "총 일수(days from 0.0.0)"로 변환**하여 비교하는 것이 가장 간편합니다.

1. **변환 함수**: `YYYY.MM.DD` -> `year * 12 * 28 + month * 28 + day`
2. **약관 매핑**: `terms`를 `{"A": 6, "B": 12}` 형태의 딕셔너리로 변환 (유효기간 달 수 -> 일 수로 변환 필요: `term * 28`).
3. **비교**:
    - `today_days` 계산.
    - 각 privacy에 대해:
        - `collected_days` 계산.
        - `expire_days` = `collected_days` + `term_months * 28` - 1 (당일까지 유효하므로)
        - 파기 조건: `today_days > expire_days` (또는 `today >= collected + term * 28`라고 생각해도 됨. 유효기간 다음날부터 파기이므로)
        - 문제 설명에는 "유효기간이 지났다면"이라고 되어 있음.
        - 예: 2021.05.02 수집, 유효기간 6달 -> 2021.11.01까지 유효. 2021.11.02부터 파기 대상.
        - 즉, `collected_days + term_days <= today_days` 이면 파기해야 함.

### 알고리즘 순서
1. `to_days(date_str)` 함수 작성.
2. `today_days` 변환.
3. `term_map` 생성 (약관 종류 -> 유효기간 월).
4. `privacies` 순회 (index `i`는 1부터 시작):
    - `date, type = privacy.split()`
    - `limit_days` = `to_days(date)` + `term_map[type] * 28`
    - 만약 `today_days >= limit_days`: 결과 리스트에 `i` 추가.
    - (주의: 수집일 포함 `term`개월이므로 단순 더하기가 맞는지 검증.
        - 1.1 수집, 1달 유효 -> 1.28까지 유효, 2.1 파기.
        - `1 * 28 + 1` + `28` = `57`.
        - `2 * 28 + 1` = `57`.
        - `today(2.1)` = `57`.
        - `57 >= 57` -> 파기. 맞음.)

## Python 코드

```python
def to_days(date_str):
    y, m, d = map(int, date_str.split('.'))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    # 오늘 날짜 변환
    today_val = to_days(today)
    
    # 약관 정보 딕셔너리
    term_map = {}
    for term in terms:
        t_type, t_period = term.split()
        term_map[t_type] = int(t_period)
        
    answer = []
    
    for i, privacy in enumerate(privacies):
        date_str, t_type = privacy.split()
        collected_val = to_days(date_str)
        
        # 유효기간 (개월 -> 일)
        period_days = term_map[t_type] * 28
        
        # 만료일 계산
        # 수집일 + 유효기간 <= 오늘 이면 파기 대상
        # 예: 5.2 수집, 6개월 -> 11.1까지 유효. 11.2(수집일+6달)부터 파기.
        # collected_val + period_days 값과 today_val을 비교
        expire_val = collected_val + period_days
        
        if today_val >= expire_val:
            answer.append(i + 1)
            
    return answer
```

## 배운 점 / 팁
- **단위 통일 (Normalization)**: 날짜/시간 문제는 가장 작은 단위(일, 초 등)로 변환하여 정수 비교로 치환하는 것이 국룰입니다.
- **모든 달이 28일**: 캘린더 라이브러리를 쓸 필요 없이 단순 곱셈으로 해결할 수 있는 힌트입니다.
