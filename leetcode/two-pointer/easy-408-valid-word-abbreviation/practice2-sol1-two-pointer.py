def solution(word, abbr):
    i=j=0
    n,m = len(word), len(abbr)

    while i<n and j<m:
        if abbr[j].isdigit():
            if abbr[j]=='0':
                return False
            skip = 0
            while j<m and abbr[j].isdigit():
                skip = skip*10 + int(abbr[j])
                j += 1
            i += skip
        else:
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i==n and j==m


input1 = ("internationalization", "i12iz4n")
# input2 = ("apple", "a2e")


print(solution(*input1))
# print(solution(*input2))
