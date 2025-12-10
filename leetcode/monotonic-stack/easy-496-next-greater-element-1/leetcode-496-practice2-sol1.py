"""
https://leetcode.com/problems/next-greater-element-i
"""
input1 = ([4,1,2], [1,3,4,2])
input2 = ([2,4], [1,2,3,4])

def solution(nums1, nums2):
    stack = []
    num2_map = {}
    for curr in range(len(nums2)):
        while stack and nums2[stack[-1]] < nums2[curr]:
            num2_map[nums2[stack.pop()]] = nums2[curr]
        stack.append(curr)

    return [num2_map.get(n1, -1) for n1 in nums1]

print(solution(*input1))
print(solution(*input2))