# class Solution:
    # def removeDuplicates(self, nums: list[int]) -> int:    
def removeDuplicates(nums):
    k = 1

    for num in range(1, len(nums)):
        if nums[num] != nums[num - 1]:
            nums[k] = nums[num]
            k += 1
    
    return k

def test_remove_duplicates():
    assert removeDuplicates([1, 2, 2, 3, 4, 4, 5]) == 5
    assert removeDuplicates([1, 2, 2, 3, 4, 4, 5, 6]) == 6
    assert removeDuplicates([1, 1, 2, 2, 2, 3, 3, 3, 3, 3]) == 3