class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, n in enumerate(nums):
            if target - n in seen:
                return [seen[target - n], i]
            seen[n] = i

        return []


if __name__ == "__main__":
    s = Solution()
    # 把 LeetCode 題目頁的 Example 直接搬過來
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
    # 自己加的 edge case
    assert s.twoSum([], 0) == []
    print("ok")
