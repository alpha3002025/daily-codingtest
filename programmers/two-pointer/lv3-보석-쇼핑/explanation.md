# 보석 쇼핑 (Gems Shopping)

## 1. 문제 설명
- **문제 링크**: [https://school.programmers.co.kr/learn/courses/30/lessons/67258](https://school.programmers.co.kr/learn/courses/30/lessons/67258)
- **정보**:
  - 진열대에 놓인 보석들의 이름이 적힌 리스트 `gems`가 주어집니다.
  - 진열대의 특정 구간을 구매하여, 진열된 **모든 종류의 보석을 적어도 1개 이상** 포함하도록 하려 합니다.
  - 조건을 만족하는 가장 짧은 구간 `[시작 번호, 끝 번호]`를 반환해야 합니다.
  - 가장 짧은 구간이 여러 개라면 시작 번호가 가장 작은 것을 선택합니다.
- **제한사항**:
  - `gems` 배열의 크기: 1 이상 100,000 이하.

---

## 2. 접근법 및 핵심 개념 (Two Pointers / Sliding Window)

### 개념: 투 포인터 (Two Pointers) & 슬라이딩 윈도우
이 문제는 연속된 구간을 찾는 문제이므로 **투 포인터(Two Pointers)** 또는 **슬라이딩 윈도우(Sliding Window)** 알고리즘이 적합합니다.
단순 이중 반복문($O(N^2)$)을 사용하면 $N=100,000$일 때 시간 초과가 발생하므로, $O(N)$ 시간 복잡도로 풀어야 합니다.

### 알고리즘 로직
1. **초기화**: `start`, `end` 두 포인터를 0으로 둡니다.
2. **확장 (End 이동)**: 
   - 구간 내에 모든 종류의 보석이 포함될 때까지 `end` 포인터를 오른쪽으로 이동시키며 보석을 추가합니다.
   - 이때 딕셔너리(Map)를 사용하여 구간 내 각 보석의 개수를 카운트합니다.
3. **축소 (Start 이동)**:
   - 모든 보석 종류를 다 모았다면, 조건을 만족하는 한에서 `start` 포인터를 오른쪽으로 이동시켜 구간을 최소화합니다.
   - `start` 위치의 보석 개수가 1보다 크다면, 하나를 빼도 종류 충족 조건은 유지되므로 `start`를 증가시킵니다.
4. **갱신**:
   - 최소 구간 조건을 만족할 때마다 정답을 갱신합니다. (길이가 더 짧거나, 길이가 같다면 시작 인덱스가 작은 것으로)

---

## 3. Python 풀이

```python
from collections import defaultdict

def solution(gems):
    # 전체 보석 종류의 개수
    kind_count = len(set(gems))
    
    # 윈도우 크기 (gems 전체 길이 + 1)
    n = len(gems)
    
    # 정답 초기화 [길이, 시작 인덱스, 끝 인덱스]
    # 길이를 무한대로 설정하여 최소값을 찾음
    answer = [n + 1, 0, 0]
    
    # 딕셔너리로 현재 구간의 보석 개수 카운트
    gem_dict = defaultdict(int)
    
    start = 0
    end = 0
    
    while True:
        # 1. 모든 보석 종류를 다 모은 경우 -> 범위를 줄여본다 (start 증가)
        if len(gem_dict) == kind_count:
            # 현재 구간이 기존 답보다 짧으면 갱신
            if (end - start) < answer[0]:
                answer = [end - start, start + 1, end]  # 1-based index 저장
            
            # start 포인터 이동 (구간 축소)
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]] # 개수가 0이면 키 삭제
            start += 1
            
        # 2. 모든 보석 종류를 못 모은 경우 -> 범위를 늘린다 (end 증가)
        elif end == n:
            # end가 끝까지 닿았는데도 부족하면 종료
            break
        else:
            # end 포인터 이동 (구간 확장)
            gem_dict[gems[end]] += 1
            end += 1
            
    return [answer[1], answer[2]]
```

### 코드 분석
- `kind_count`: 구해야 할 총 보석의 종류 수입니다. `len(set(gems))`로 계산합니다.
- `start`, `end`: 윈도우의 시작과 끝을 가리키는 포인터입니다. `[start, end)` (반열린 구간) 방식을 사용하여 구현했습니다.
- `gem_dict`: 현재 윈도우 안에 들어있는 보석들의 개수를 저장합니다. `len(gem_dict)`가 `kind_count`와 같다면 모든 보석을 다 포함한 상태입니다.
- **While 루프**:
    - `len(gem_dict) == kind_count` (조건 만족) 일 때:
        - 현재 길이가 최소인지 확인하고 `answer` 갱신.
        - `start`에 있는 보석을 하나 빼고 `start`를 오른쪽으로 한 칸 이동합니다.
    - `len(gem_dict) != kind_count` (조건 불만족) 일 때:
        - `end`가 범위를 벗어나면 종료.
        - 그렇지 않으면 `gems[end]`를 추가하고 `end`를 오른쪽으로 한 칸 이동합니다.

---

## 4. 복잡도 분석
- **시간 복잡도**: $O(N)$
  - `start`와 `end` 포인터는 각각 최대 $N$번씩 증가합니다.
  - 따라서 배열을 최대 2번 훑는 셈이 되므로 선형 시간 복잡도($O(N)$)를 가집니다.
  - $N=100,000$이므로 충분히 효율적입니다.
- **공간 복잡도**: $O(M)$ (M: 보석 종류의 수)
  - 딕셔너리(`gem_dict`)에 저장되는 키의 개수는 보석의 종류 수만큼입니다.
