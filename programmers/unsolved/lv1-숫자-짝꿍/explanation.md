# 숫자 짝꿍

## 문제 설명
[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/131128)

두 정수 `X`, `Y`의 공통된 숫자들(짝꿍)을 모아 만들 수 있는 **가장 큰 정수**를 반환하세요.
- 공통인 숫자가 없으면 `"-1"`
- 공통인 숫자가 `0`뿐이면 `"0"` (예: "00" -> "0")
- 결과는 문자열로 반환.

## 해결 전략
두 문자열 `X`, `Y`에서 각 숫자(0~9)가 몇 번씩 등장하는지 카운트합니다.
공통으로 사용할 수 있는 개수는 `min(X에서의 개수, Y에서의 개수)`입니다.
가장 큰 수를 만들어야 하므로, **9부터 0까지** 역순으로 확인하며 가능한 만큼 이어 붙입니다.

### 알고리즘 순서
1. `X`, `Y`의 각 숫자 빈도수(Counter) 계산. (딕셔너리 or 리스트 `[0]*10`)
2. `result` = ""
3. 9부터 0까지 `i` 반복:
    - `common_count = min(X.count(i), Y.count(i))`
    - `result += str(i) * common_count`
4. 예외 처리:
    - `result`가 비어있으면 `"-1"`
    - `result`의 첫 글자가 `"0"`이면(즉 "000..."), `"0"`
5. 반환.

## Python 코드

```python
def solution(X, Y):
    answer = ''
    
    # 0~9 각 숫자의 개수 세기 (문자열 count 메서드 활용)
    # X, Y 길이가 매우 길면(300만), Counter 객체가 더 효율적일 수 있으나
    # 여기서는 고정된 10개 숫자에 대해 count하므로 O(N) 동일
    
    # x_cnt = {str(i): X.count(str(i)) for i in range(10)} # 시간이 조금 더 걸릴 수 있음
    
    # collections.Counter 사용이 가장 효율적
    from collections import Counter
    cnt_x = Counter(X)
    cnt_y = Counter(Y)
    
    # 9부터 0까지 내림차순으로 확인 (큰 수 만들기 위해)
    for i in range(9, -1, -1):
        key = str(i)
        if key in cnt_x and key in cnt_y:
            # 둘 중 적은 개수만큼 짝지을 수 있음
            common = min(cnt_x[key], cnt_y[key])
            answer += key * common
            
    if not answer:
        return "-1"
        
    # "000" -> "0" 처리
    if answer[0] == "0":
        return "0"
        
    return answer
```

## 배운 점 / 팁
- **큰 수 만들기 전략**: 자릿수가 정해지지 않은 조합 문제에서 "가장 큰 수"를 만들려면 큰 숫자(9)를 앞에서부터 최대한 많이 채우면 됩니다.
- **문자열 vs 정수**: 결과값이 매우 클 수 있으므로(길이 300만), 절대 정수로 변환(`int()`)하려 하면 안 되고 문자열 상태로 처리해야 합니다.
- **예외 처리 디테일**: `0`만 여러 개일 때 `00`이 아니라 `0`이어야 한다는 점을 놓치기 쉽습니다.
