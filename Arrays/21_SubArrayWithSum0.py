class Solution:
    def SubArraySum0(self,arr,n):
        sum = 0
        bool = False
        for i in range(n):
            sum = sum + arr[i]
            if sum == 0 or arr[i]==0:
                bool = True
            else:
                bool = False
        return bool

if __name__=='__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    if obj.SubArraySum0(arr,N):
        print('Yes')
    else:
        print('No')
    