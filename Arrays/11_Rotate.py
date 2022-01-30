
class Solution:
    def Rotate(self,arr,n):
        x = arr[n-1]
       
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = x
        return arr

if __name__=='__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.Rotate(arr,N)
    for i in result:
        print(i , end=' ')