class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers.sort()
        l = 0
        r = len(numbers) - 1

        while l < r:
            twosum = numbers[r] + numbers[l]

            if twosum == target:
                return [l+1, r+1]
            
            elif twosum > target:
                r -= 1
            
            else:
                l += 1
        
        return False