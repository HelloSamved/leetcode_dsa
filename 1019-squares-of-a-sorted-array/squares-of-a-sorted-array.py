class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n= len(nums)
        neg=[]
        pos=[]
        
        for num in nums:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        
        if len(neg)==0:
            return [x*x for x in pos]
        if len(pos)==0:
            result= [x*x for x in neg]
            result.reverse()
            return result
        
        neg= [x*x for x in neg][::-1]
        pos= [x*x for x in pos]
        result=[]
        n,m= len(neg), len(pos)
        i=0
        j=0
        while i<n and j<m:
            if neg[i]<= pos[j]:
                result.append(neg[i])
                i+=1
            else:
                result.append(pos[j])
                j += 1
            
        while i<n:
            result.append(neg[i])
            i+=1
        while j<m:
            result.append(pos[j])
            j+=1
        
        return result