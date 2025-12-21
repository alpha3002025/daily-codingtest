# 로또의 최고 순위와 최저 순위

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/77484)

구매한 로또 번호 `lottos` 중 일부가 지워져 `0`으로 보입니다.
당첨 번호 `win_nums`와 비교하여:
- **최고 순위**: `0`이 모두 당첨 번호라고 가정했을 때
- **최저 순위**: `0`이 모두 꽝이라고 가정했을 때
각각의 등수를 구하세요. (6개 일치: 1등, ..., 1개 이하: 6등)

## 해결 전략
1. 현재 눈에 보이는 일치 개수 `cnt`를 셉니다.
2. `0`의 개수 `zeros`를 셉니다.
3. 최고 일치 수 = `cnt + zeros`
4. 최저 일치 수 = `cnt`
5. 등수 변환: `7 - 일치수` (단, 일치수가 1 이하이면 6등).
    - `grade = [6, 6, 5, 4, 3, 2, 1]` 배열을 써도 됨.

### 알고리즘 순서
1. `cnt` = `lottos`와 `win_nums`의 교집합 크기 (또는 루프).
2. `zeros` = `lottos.count(0)`
3. `max_correct = cnt + zeros`
4. `min_correct = cnt`
5. `rank` 함수 정의: `min(6, 7 - correct)`
6. 반환 `[rank(max), rank(min)]`.

## Python 코드

```python
def solution(lottos, win_nums):
    # 등수 매핑 테이블 (인덱스: 맞춘 개수 -> 값: 등수)
    # 0개->6등, 1개->6등, 2개->5등, ... 6개->1등
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    cnt = 0
    zeros = 0
    
    for num in lottos:
        if num == 0:
            zeros += 1
        elif num in win_nums:
            cnt += 1
            
    max_correct = cnt + zeros
    min_correct = cnt
    
    return [rank[max_correct], rank[min_correct]]
```

## 배운 점 / 팁
- **Best/Worst Case**: 미지수(`0`)가 모두 성공일 때와 모두 실패일 때를 각각 가정하여 범위를 구하는 문제입니다.
- **Lookup Table**: 복잡한 `if-else` 대신 배열 인덱싱을 사용하면 코드가 깔끔해집니다.
