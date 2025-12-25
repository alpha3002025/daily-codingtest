import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while scoville:
        curr = heapq.heappop(scoville)
        
        if curr < K:
            if scoville:
                second = heapq.heappop(scoville)
                result = curr + (2*second)
                heapq.heappush(scoville, result)
                cnt += 1
            else:
                return -1
        else:
            return cnt
    
    return -1