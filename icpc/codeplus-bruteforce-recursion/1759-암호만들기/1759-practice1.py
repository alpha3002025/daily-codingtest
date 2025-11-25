import sys

L,C = map(int, sys.stdin.readline().split())
char_list = sorted(sys.stdin.readline().split())
vowels = set('aeiou')


"""
L 길이의 문자를 만드는데 C 종류의 문자를 사용한다.
모음(vowels) 은 최소 1개 포함해야 하고
자음(not_vowels) 는 최소 2 개 포함되어야 한다.
"""
def backtrack(curr, password, vowels_count, not_vowels_count):
    if len(password) == L:
        if vowels_count >=1 and not_vowels_count >= 2:
            print(''.join(password))
        return
    
    for ci in range(curr, C):
        is_vowel = char_list[ci] in vowels
        backtrack(
            ci+1,
            password + [char_list[ci]],
            vowels_count + (1 if is_vowel else 0),
            not_vowels_count + (0 if is_vowel else 1)
        )


backtrack(0, [], 0, 0)