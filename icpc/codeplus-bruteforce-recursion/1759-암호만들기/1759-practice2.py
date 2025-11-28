import sys
input = sys.stdin.readline

L,C = map(int, input().split())
chars = sorted(input().split())
vowels = set('aeiou')

def backtracking(curr_idx, curr_list, vowel_count, not_vowel_count):
    if len(curr_list) == L:
        if vowel_count >= 1 and not_vowel_count >= 2:
            print(''.join(curr_list))
        return

    for i in range(curr_idx, len(chars)):
        c = chars[i]
        backtracking(
            i+1, 
            curr_list + [c],
            vowel_count if c not in vowels else vowel_count+1,
            not_vowel_count if c in vowels else not_vowel_count+1
        )

backtracking(0, [], 0, 0)