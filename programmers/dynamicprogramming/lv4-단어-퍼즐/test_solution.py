def solution(strs, t):
    # strs의 단어들을 빠른 조회를 위해 set으로 변환
    word_set = set(strs)
    n = len(t)

    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # 1부터 t의 길이 n까지 순회
    for i in range(1, n + 1):
        # k는 1~5를 돌되, i-k >= 0 조건을 체크하는 것이 안전
        for k in range(1, 6):
            if i - k < 0:
                # 더 이상 뒤로 갈 수 없으면 종료 (k가 커질수록 더 뒤를 보므로)
                break
            
            # t의 끝부분(길이 k) 문자열 추출
            # t는 0-based 인덱스이므로
            # 길이 i까지의 부분문자열은 t[:i]이고, 
            # 거기서 뒤의 k개를 자르면 t[i-k : i]가 됨
            sub = t[i-k : i]
            
            if sub in word_set:
                # 이전 상태(dp[i-k])가 유효하다면(만들 수 있는 상태라면)
                if dp[i-k] != float('inf'):
                    dp[i] = min(dp[i], dp[i-k] + 1)
                    
    # 만들 수 없는 경우(여전히 INF) -1 반환
    if dp[n] == float('inf'):
        return -1
        
    return dp[n]


input1 = (["ba","na","n","a"], "banana")
input2 = (["app","ap","p","l","e","ple", "pp"], "apple")
input3 = (["ba","an","nan", "ban", "n"], "banana")

print(solution(*input1))
# print(solution(*input2))
# print(solution(*input3))
