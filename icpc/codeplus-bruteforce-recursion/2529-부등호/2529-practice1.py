def solve():
    k = int(input())
    signs = input().split()

    used = [False] * 10
    max_num = ""
    min_num = ""

    def is_valid(a, b, sign):
        if sign == '<':
            return a < b
        else:
            return a > b
        
    def backtrack(depth, num_str):
        nonlocal max_num, min_num

        if depth == k+1:
            if not min_num:
                min_num = num_str
            max_num = num_str
            return
        
        for i in range(10):
            if used[i]:
                continue

            if depth == 0 or is_valid(int(num_str[-1]), i, signs[depth -1]):
                used[i] = True
                backtrack(depth+1, num_str + str(i))
                used[i] = False
    
    backtrack(0, "")
    print(max_num)
    print(min_num)

solve()