"""
test (1) : split_uv("(()())") = ('(()())', '')
test (2) : split_uv(")(") = (')(', '')
test (3) : split_uv("()))((()") = ('()', '))((()')
test (4) : split_uv("()()()()") = ('()', '()()()')
"""


def split_uv(p):
    """문자열을 u, v로 분리"""
    count_l = 0
    count_r = 0
    for i in range(len(p)):
        if p[i] == '(':
            count_l += 1
        else:
            count_r += 1
            
        if count_l == count_r:
            return p[:i+1], p[i+1:]
    return p, ""

print(f'test (1) : split_uv("(()())") = {split_uv("(()())")}')
print(f'test (2) : split_uv(")(") = {split_uv(")(")}')
print(f'test (3) : split_uv("()))((()") = {split_uv("()))((()")}')
print(f'test (4) : split_uv("()()()()") = {split_uv("()()()()")}')

s = 'abcde'
print(f"abcde[5:] = {s[5:]}")
