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
    min_distance = float('inf')
    start,end = 0,0
    window = [start, end]
    
    occurrence = defaultdict(int)
    kind = set(gems)
    kind_cnt = len(kind)
    
    while True:
        ### 조심!!) 탈출 조건문을 맨 앞에 두면, 보석이 들어있어서 윈도우를 줄일 여지가 있어도 break 할때가 있다.
        # if end == len(gems):
        #     break
        
        # elif len(occurrence) == kind_cnt:
        if len(occurrence) == kind_cnt:
            ## 원하는 종류수를 채웠으면? => 윈도우를 줄여본다.
            # start += 1
            
            if min_distance > end - start:
                min_distance = end - start

                window = [start+1, end]

            occurrence[gems[start]] -= 1
            if occurrence[gems[start]] == 0:
                del occurrence[gems[start]]

            start += 1
            
        elif end == len(gems):
            break
        
        else:
            ## 종류수를 아직 못채웠으면? => 새로운 item 을 탐색한다.
            # end += 1
            
            occurrence[gems[end]] += 1
            end += 1
    
    return window
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

## Q & A

### Q1. `if end == len(gems): break` 구문을 `while` 문 맨 처음에 두었을 때 오답이 발생하는 이유와 예시는?

두 코드는 `break` 문을 포함한 **조건문의 배치 순서** 때문에 하나는 정답이 되고, 다른 하나는 오답이 됩니다. 핵심은 **조건을 만족하는 경우(윈도우 축소)를 `end` 체크보다 상위에 두어야 한다**는 점입니다.

#### 1. 에러 발생 원인
`end`가 리스트의 끝(`len(gems)`)에 도달했더라도, 현재 윈도우(`start` ~ `end`) 안에 불필요한 보석이 포함되어 있을 수 있습니다. 이때 `break`를 먼저 해버리면, **마지막으로 윈도우를 축소하여 최솟값을 갱신할 기회를 잃어버리게 됩니다.**

#### 2. 반례 예시
`gems = ["A", "A", "B", "C"]` (종류: 3개) 일 때를 가정해 봅시다.

**정상 로직 (축소 먼저 체크):**
1. `end`가 4까지 이동하여 `['A', 'A', 'B', 'C']` (길이 4)를 모두 포함합니다.
2. 루프 진입 시 `len(gem_dict) == 3` (조건 만족)을 먼저 체크합니다.
3. `start`를 이동시켜 맨 앞의 `A`를 제거합니다. → `['A', 'B', 'C']` (길이 3)
4. **최단 구간 길이 갱신 (4 → 3)** 성공.

**오류 로직 (`end` 체크 먼저):**
1. `end`가 4까지 이동하여 `['A', 'A', 'B', 'C']`를 포함합니다.
2. 루프 진입 시 `if end == 4:`를 먼저 만나서 **즉시 종료(`break`)** 됩니다.
3. 맨 앞의 `A`를 제거하는 축소 과정을 수행하지 못함.
4. **최단 구간 길이는 여전히 4**로 남게 되어 **오답** 처리됩니다.

따라서 종료 조건은 **"더 이상 확장할 수도 없고(끝 도달), 줄일 수도 없을 때(조건 불만족)"** 수행되어야 합니다.




