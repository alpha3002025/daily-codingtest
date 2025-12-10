"""
https://leetcode.com/problems/remove-k-digits/
"""
def solution(number, k):
    stack = []
    for c in number:
        ## Greedy 로직
        ##   스택의 top 이 현재숫자보다 크면 제거
        ##   이전 값이 현재값보다 크다면, 바로 이전 자리가 더 큰수였다는 이야기
        while k>0 and stack and stack[-1] > c:
            stack.pop()
            k-=1
        stack.append(c)

    ## 만약 k 가 아직 남아있다면, 뒤에서부터 제거
    ## (이미 숫자는 오름차순 형태일 것이기에(k만큼의 큰수를 제거했기에), 뒤쪽이 k개의 수가 큰수다.)
    ## 솔직히 이 부분은 아직 이해 못했다.
    if k > 0:
        stack = stack[:-k]
    
    ## 문자열로 변환 & 앞쪽 '0' 제거
    s = "".join(stack).lstrip("0")

    ## 빈 문자열일 경우 '0' 반환
    if s:
        return s
    return "0"

input1 = ("1432219", 3)
input2 = ("10200", 1)
input3 = ("10", 2)

print(solution(*input1))
print(solution(*input2))
print(solution(*input3))