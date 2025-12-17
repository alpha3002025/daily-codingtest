"""
gemini provided
"""
import heapq

def solution(scoville, K):
    # 최소 힙으로 변환
    heapq.heapify(scoville)
    mix_count = 0
    
    # 가장 맵지 않은 음식(root)이 K 미만일 때 계속 반복
    while scoville[0] < K:
        # 음식이 하나밖에 안 남았는데 K 미만이면 불가능
        if len(scoville) < 2:
            return -1
            
        # 가장 작은 2개 추출
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 섞어서 다시 넣기
        new_food = first + (second * 2)
        heapq.heappush(scoville, new_food)
        
        mix_count += 1
        
    return mix_count