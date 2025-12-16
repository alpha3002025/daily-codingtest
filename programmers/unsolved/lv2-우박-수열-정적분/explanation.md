# 우박 수열 정적분

## 문제 설명
콜라츠 추측(Collatz Conjecture)에 따라 우박 수열을 만듭니다.
- 짝수면 2로 나눔, 홀수면 3을 곱하고 1을 더함. 1이 될 때까지 반복.
수열을 그래프 `(x, y)` 점으로 찍고, 인접한 점 사이를 직선으로 연결합니다.
주어진 구간 `[a, b]`에 대한 정적분 결과(그래프 아랫부분 면적)를 구하는 문제입니다.
단, 구간 `[a, b]`에서 `b`는 끝점에서부터의 오프셋(음수)으로 주어집니다.

## 풀이 개념
**구현**과 **누적 합 (Prefix Sum)**을 사용하면 효율적입니다.

1. **수열 생성**: 주어진 `k`로 우박 수열(y값 리스트)을 만듭니다.
2. **단위 면적 계산**: 각 구간 `[i, i+1]`의 면적은 사다리꼴 넓이 공식 `(y[i] + y[i+1]) / 2` 입니다.
3. **누적 합**: 면적들을 구하면서 누적 합 배열을 만듭니다. `prefix_area[i]`는 0부터 `i`까지의 총 면적.
4. **구간 쿼리 처리**:
   - 입력 범위 `[a, b]`를 실제 인덱스로 변환: 시작 `x1 = a`, 끝 `x2 = n + b` (n은 수열 길이-1).
   - `x1 > x2`인 경우 유효하지 않은 구간이므로 -1.0 반환.
   - 면적은 `prefix_area[x2] - prefix_area[x1]`로 O(1)에 계산.

## 코드 (Python)

```python
def solution(k, ranges):
    # 1. 우박 수열 생성
    sequence = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        sequence.append(k)
        
    n = len(sequence) - 1 # x 좌표의 끝 (구간의 개수)
    
    # 2. 누적 면적 계산
    # prefix_area[i] : 0부터 i까지 구간의 누적 면적
    prefix_area = [0.0] * (n + 1)
    
    for i in range(n):
        # 사다리꼴 넓이: (윗변 + 아랫변) * 높이 / 2, 높이는 1
        area = (sequence[i] + sequence[i+1]) / 2
        prefix_area[i+1] = prefix_area[i] + area
        
    answer = []
    
    for a, b in ranges:
        # 실제 구간 인덱스 계산
        start, end = a, n + b
        
        if start > end:
            answer.append(-1.0)
        else:
            # 정적분 결과 = 누적 면적의 차
            result = prefix_area[end] - prefix_area[start]
            answer.append(result)
            
    return answer
```
