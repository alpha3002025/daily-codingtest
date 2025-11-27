N = int(input())
W = list(map(int, input().split()))

def solve(energy, removed_count):
    if removed_count == len(energy)-2:
        return 0
    
    max_energy = 0

    for i in range(1, len(energy)-1):
        if energy[i] == -1:
            continue

        left = i-1
        while left >= 0 and energy[left] == -1:
            left -= 1

        right = i+1
        while right < len(energy) and energy[right] == -1:
            right += 1

        # 에너지 계산
        gained = energy[left] * energy[right]

        original = energy[i]
        energy[i] = -1

        total = gained + solve(energy, removed_count + 1)

        energy[i] = original
        max_energy = max(max_energy, total)
    
    return max_energy

print(solve(W,0))