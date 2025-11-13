import sys
sys.setrecursionlimit(1000001)
from collections import defaultdict

def solution(sales, links):
    # 인접 리스트 구성
    children = defaultdict(list)
    for u, v in links:
        children[u].append(v)
    
    print(f"sales = {sales}")
    print(f"links = {links}")
    print(f"children = {children}")
    
    # DP: A[u] = u 선택, B[u] = u 미선택
    def dfs(u):
        # 말단 직원 (자식 없음)
        if not children[u]:
            return sales[u-1], 0
        
        # 자식들 먼저 계산
        child_results = [dfs(v) for v in children[u]]
        print(f"u = {u}, child_results = {child_results}")
        
        # A[u]: u를 선택하면, 자식들은 자유롭게 선택
        a = sales[u-1] + sum(min(a_v, b_v) for a_v, b_v in child_results)
        
        # B[u]: u를 선택 안하면, 최소 1명의 자식은 반드시 선택
        # 모든 자식을 "자유롭게" 선택한 후, 한 명은 "강제로" 선택
        total = sum(min(a_v, b_v) for a_v, b_v in child_results)
        # 각 자식을 강제 선택했을 때의 추가 비용 중 최소값
        min_extra = min(a_v - min(a_v, b_v) for a_v, b_v in child_results)
        b = total + min_extra
        
        return a, b
    
    a1, b1 = dfs(1)
    return min(a1, b1)

result1 = solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]])
print(f"result1 = {result1}")
