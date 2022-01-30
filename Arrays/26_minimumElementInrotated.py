class Solution:
    def minimumElementInrotated(self,a,n):
        return min(a)

if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.minimumElementInrotated(arr,n)
    print(result)












