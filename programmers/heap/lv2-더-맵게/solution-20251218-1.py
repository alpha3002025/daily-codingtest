from heapq import heappush, heappop

def solution(scoville, K):
    A = []
    for s in scoville:
        heappush(A, s)
    
    cnt = 0
    prev = heappop(A)
    
    while A and prev < K:
        score = prev + 2 * heappop(A)
        cnt += 1
        heappush(A, score)
        prev = heappop(A)
    
    if prev < K:
        return -1
    return cnt