# 광물 캐기

## 문제 설명
다이아몬드, 철, 돌 곡괭이가 0 ~ 5개씩 주어집니다.
곡괭이로 광물을 캘 때 피로도가 소모됩니다.
- 다이아 곡괭이: 다이아(1), 철(1), 돌(1)
- 철 곡괭이: 다이아(5), 철(1), 돌(1)
- 돌 곡괭이: 다이아(25), 철(5), 돌(1)
각 곡괭이는 5개의 광물을 캐면 부러집니다. 광물은 주어진 순서대로 캐야 합니다.
최소 피로도를 구하는 문제입니다. 곡괭이가 없거나 광물이 없으면 종료합니다.

## 풀이 개념
**그리디 알고리즘**과 **정렬**을 사용합니다.
광물을 순서대로 캐야 하지만, **어느 곡괭이를 사용할지는 선택**할 수 있습니다.
한 번 곡괭이를 선택하면 5개를 연속으로 캐야 하므로, 광물들을 **5개씩 묶어서(Chunk)** 생각합니다.

1. **캘 수 있는 광물 제한**: 곡괭이 개수의 총합에 5를 곱한 만큼만 광물을 캘 수 있습니다. 만약 광물이 더 많다면, 뒤쪽 광물은 어차피 못 캐므로 잘라냅니다.
2. **그룹화 및 가중치 계산**: 남은 광물들을 5개씩 묶고, 각 묶음의 중요도(피로도 가중치)를 계산합니다.
   - 이때 "돌 곡괭이"로 캘 때의 피로도를 기준으로 계산하면 해당 묶음이 얼마나 처리가 어려운지 알 수 있습니다.
   - (다이아 25, 철 5, 돌 1 가중치 적용).
3. **정렬**: 피로도가 높은(어려운) 묶음부터 처리하기 위해 내림차순 정렬합니다.
4. **곡괭이 할당**: 가장 어려운 묶음에는 가장 좋은 곡괭이(다이아 > 철 > 돌)를 할당하여 피로도를 최소화합니다.

## 코드 (Python)

```python
def solution(picks, minerals):
    # 캘 수 있는 최대 광물 수
    total_picks = sum(picks)
    if total_picks == 0:
        return 0
    
    # 곡괭이로 캘 수 있는 만큼만 광물 자르기
    minerals = minerals[:total_picks * 5]
    
    # 5개씩 묶어서 (돌 곡괭이 기준 피로도, 묶음 내용) 저장
    chunks = []
    for i in range(0, len(minerals), 5):
        chunk = minerals[i:i+5]
        cost = 0
        for m in chunk:
            if m == "diamond": cost += 25
            elif m == "iron": cost += 5
            else: cost += 1
        chunks.append((cost, chunk))
    
    # 피로도가 높은(캐기 힘든) 순서대로 정렬
    chunks.sort(key=lambda x: x[0], reverse=True)
    
    answer = 0
    # 좋은 곡괭이부터 소진
    # picks[0]: dia, picks[1]: iron, picks[2]: stone
    for _, chunk in chunks:
        if picks[0] > 0:
            pick_type = 0
            picks[0] -= 1
        elif picks[1] > 0:
            pick_type = 1
            picks[1] -= 1
        elif picks[2] > 0:
            pick_type = 2
            picks[2] -= 1
        else:
            break
            
        # 선택된 곡괭이로 피로도 계산
        for m in chunk:
            if pick_type == 0: # Dia pick
                answer += 1
            elif pick_type == 1: # Iron pick
                if m == "diamond": answer += 5
                else: answer += 1
            else: # Stone pick
                if m == "diamond": answer += 25
                elif m == "iron": answer += 5
                else: answer += 1
                
    return answer
```
