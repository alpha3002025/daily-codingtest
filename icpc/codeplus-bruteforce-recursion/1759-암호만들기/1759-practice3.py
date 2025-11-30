import sys
input = sys.stdin.readline

L,C = map(int, input().split())
chars = sorted(list(input().split()))
vowels = set('aeiou')


def dfs(curr_idx, curr_chars):
    if len(curr_chars) == L:
        vowels_count = len([c for c in curr_chars if c in vowels])
        not_vowels_count = len([c for c in curr_chars if c not in vowels])
        if vowels_count >= 1 and not_vowels_count >= 2:
            print(''.join(curr_chars))
    
    for i in range(curr_idx, C):
        dfs(i+1, curr_chars + [chars[i]])

dfs(0, [])