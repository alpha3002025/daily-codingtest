# 가장 긴 팰린드롬

## 문제 설명
문자열 `s`의 부분 문자열 중 가장 긴 팰린드롬의 길이를 구하세요.

## 문제 해결 전략

$N \le 2500$ 이므로 $O(N^2)$ 알고리즘 사용 가능합니다.
**중심 확장법 (Expand Around Center)**:
- 문자열의 각 위치를 중심으로 잡고 좌우로 확장하며 팰린드롬 여부를 확인합니다.
- 중심은 문자 1개일 수도(홀수 길이), 문자 사이일 수도(짝수 길이) 있습니다.
  - Case 1: `i`를 중심으로 (예: `aba`)
  - Case 2: `i, i+1` 사이를 중심으로 (예: `abba`)

## Python 코드

```python
def solution(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # while문에 의해 한 칸 더 갔으므로 길이보정
        # (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1

    if len(s) < 2:
        return len(s)
        
    answer = 0
    for i in range(len(s) - 1):
        # 홀수 길이
        len1 = expand(i, i)
        # 짝수 길이
        len2 = expand(i, i + 1)
        answer = max(answer, len1, len2)
        
    return answer
```
