# 题目：nums = [2, 7, 11, 15], target = 9 → 返回 [0, 1]（因为 nums[0] + nums[1] == 9）。

def two_sum(nums,target):
    seen = {}
    for i,num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need],i]
        seen[num] = i
    return [] 
# 自测
if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    print("PASS  0001_two_sum")
