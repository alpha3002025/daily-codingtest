N = int(input())
W = list(map(int, input().split()))

def solve(energy):
    ## 더 이상 쪼갤수 없는 레벨
    ## 구슬이 2개 남았을때가 가운데 구슬을 구할수 없는 레벨
    if len(energy) == 2:
        return 0
    

    max_energy = 0

    for i in range(1, len(energy)-1): ## i=1 ~ n-2 일때 i=0,i=n 이 계산되도록
        gained = energy[i-1] * energy[i+1] ## i 번째 구슬 제거시 얻는 에너지
        new_energy = energy[:i] + energy[i+1:] ## i 번째 구슬을 제외하고 새로운 리스트 병합
        total = gained + solve(new_energy)
        max_energy = max(max_energy, total)
    
    return max_energy

print(solve(W))