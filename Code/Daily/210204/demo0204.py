def func(self, nums: List[int], k: int) -> float:
    t = len(nums) - k
    val = 0
    for i in range(0, k):
        val = val + nums[i]
    temp = val
    for i in range(0, t):
        val = val - nums[i] + nums[i + k]
        if val > temp:
            temp = val

    return temp / k


