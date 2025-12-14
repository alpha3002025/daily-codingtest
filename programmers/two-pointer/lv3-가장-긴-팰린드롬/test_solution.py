def solution(s):
    if len(s) < 2 or s == s[::-1]:
        return len(s)

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_len = 0
    for i in range(len(s) - 1):
        max_len = max(max_len, expand(i, i), expand(i, i + 1))

    return max_len


def test_solution():
    test_cases = [
        ("abcdcba", 7),
        ("abacde", 3),
        ("a", 1),
        ("aa", 2),
        ("abba", 4),
        ("abcde", 1)
    ]
    
    for s, expected in test_cases:
        result = solution(s)
        print(f"Input: {s}, Expected: {expected}, Got: {result}, {'PASS' if result == expected else 'FAIL'}")

if __name__ == "__main__":
    test_solution()
