class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            string= str(x)
            actual_list= list(string)
            reversed_list= list(string)
            reversed_list.reverse()
            if actual_list==reversed_list:
                return True
            else:
                return False