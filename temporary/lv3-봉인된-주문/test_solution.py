def solution(n, bans):
    # Precompute cumulative counts for lengths 1 to 11
    # count[k] = number of strings with length <= k
    # 26^1 + 26^2 + ... + 26^k
    cum_counts = [0] * 12
    current_sum = 0
    pow26 = [1] * 12
    for i in range(1, 12):
        pow26[i] = pow26[i-1] * 26
        current_sum += pow26[i]
        cum_counts[i] = current_sum

    def str_to_val(s):
        L = len(s)
        val = cum_counts[L-1]
        
        # Calculate rank within length L (0-based)
        rank = 0
        for i, char in enumerate(s):
            digit = ord(char) - ord('a')
            rank += digit * pow26[L - 1 - i]
        
        # Add 1 because we want 1-based index
        return val + rank + 1

    def val_to_str(v):
        # Find length L
        L = 1
        while L <= 11:
            if v <= cum_counts[L]:
                break
            L += 1
        
        # Get rank within length L (0-based)
        rank = v - cum_counts[L-1] - 1
        
        # Convert rank to base 26 string
        chars = []
        for i in range(L):
            power = pow26[L - 1 - i]
            digit = rank // power
            chars.append(chr(digit + ord('a')))
            rank %= power
        
        return "".join(chars)

    # Convert bans to integers
    ban_vals = []
    for b in bans:
        ban_vals.append(str_to_val(b))
    
    ban_vals.sort()
    
    # Calculate target index
    # We want the n-th value in the set (All - Bans)
    # Let the result value be x.
    # The number of valid items <= x is x - (count of bans <= x)
    # We want x - (count of bans <= x) = n
    # Start with x = n. Increment x for every ban that is <= x.
    
    curr = n
    for b in ban_vals:
        if b <= curr:
            curr += 1
        else:
            break
            
    return val_to_str(curr)

# Test cases
print(solution(30, ["d", "e", "bb", "aa", "ae"])) # Expected: "ah"
print(solution(7388, ["gqk", "kdn", "jxj", "jxi", "fug", "jxg", "ewq", "len", "bhc"])) # Expected: "jxk"
