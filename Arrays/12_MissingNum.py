class Solution:
    def MissingNum(self,arr,n):
        # get the array's length
        # n = len(arr)
    
        # actual size is `n+1` since a number is missing from the list
        m = n 
    
        # get a sum of integers between 1 and `n+1`
        total = m * (m + 1) // 2
    
        # the missing number is the difference between the expected sum and
        # the actual sum of integers in the list
        Missing =  total - sum(arr)
        return Missing
    
 

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.MissingNum(arr,N)
    print(result)