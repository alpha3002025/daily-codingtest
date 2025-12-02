import sys

N = int(input())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort()

M = int(input())
queries = list(map(int, sys.stdin.readline().split()))

def binarysearch(target):
    left,right = 0, len(cards)-1

    while left <= right:
        mid = (left + right)//2
        if cards[mid] == target:
            return True
        elif cards[mid] > target:
            right = mid-1
        elif cards[mid] < target:
            left = mid+1
    
    return False


for query in queries:
    result = binarysearch(query)
    print(1 if result else 0, end = ' ')
