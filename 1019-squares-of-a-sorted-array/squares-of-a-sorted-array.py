class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        output_list=[]
        for i in nums:
            output_list.append(i**2)
        output_list.sort()
        return output_list