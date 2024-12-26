# Given arr nums of integers >= 0, you can split nums into m non-empty contiguous subarrays
# Minimize the largest sum among the m subarrays
def main():
    nums = [7, 2, 5, 10, 8]
    m = 2
    l = max(nums)
    r = sum(nums)
    ans = r
    while l <= r:
        mid = (l + r) // 2
        if foundSplit(mid, nums, m):
            ans = mid
            r = mid-1
        else:
            l = mid+1
    print(ans)

def foundSplit(largest, nums, m):
    subarr_count = 1
    subarr_sum = 0
    for num in nums:
        subarr_sum += num
        if subarr_sum > largest:
            subarr_count += 1
            subarr_sum = num
    if subarr_count <= m:
        return True
    else:
        return False

if __name__ == '__main__':
    main()