input1 = ("1432219", 3)
input2 = ("10200", 1)
input3 = ("10", 2)

def solution(num, k):
    prev_stack = []
    for c in num:
        while k and prev_stack and prev_stack[-1] > c:
            prev_stack.pop()
            k-=1
        prev_stack.append(c)

    if k > 0:
        prev_stack = prev_stack[:-k]

    s = "".join(prev_stack).lstrip("0")
    return s if s else "0"


assert solution(*input1) == "1219"
assert solution(*input2) == "200"
assert solution(*input3) == "0"