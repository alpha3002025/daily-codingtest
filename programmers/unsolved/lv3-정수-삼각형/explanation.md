# 정수 삼각형

## 문제 설명
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우를 찾으세요.
아래 칸으로 이동할 때는 대각선 방향으로 한 칸 오른쪽 또는 왼쪽으로만 이동 가능합니다.

## 문제 해결 전략

**다이나믹 프로그래밍 (DP)** 기본 문제입니다.
위에서 아래로 내려오면서 값을 누적시킵니다.
`dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])`
(경계 조건 처리 필요: 맨 왼쪽은 위에서 맨 왼쪽만 오고, 맨 오른쪽은 위에서 맨 오른쪽만 옴)

## Python 코드

```python
def solution(triangle):
    # triangle 자체를 dp 테이블로 사용 (In-place)
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])
```
