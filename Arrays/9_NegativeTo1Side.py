

class Solution:
    def NegativeTo1Side(self,arr,N):
        temp = arr[0]
        j =0
        for i in range(N):
            if arr[i]>0:
                if i!=j:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                j+=1
    
        return arr
        

if __name__=='__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    obj.NegativeTo1Side(arr,N)
    print(*arr)
    
