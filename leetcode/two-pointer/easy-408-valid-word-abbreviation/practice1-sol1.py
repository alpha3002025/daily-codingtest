class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        n, m = len(word), len(abbr)
        
        while i < n and j < m:
            if abbr[j].isdigit():
                # leading zeros not allowed
                if abbr[j] == '0':
                    return False
                # read the full number
                skip = 0
                while j < m and abbr[j].isdigit():
                    skip = skip * 10 + int(abbr[j])
                    j += 1
                i += skip
            else:
                # must match the character
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        
        # both must reach the end
        return i == n and j == m