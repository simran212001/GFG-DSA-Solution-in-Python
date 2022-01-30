class Solution:
    def AlternatePositiveNegative(self,arr,n):
        neg=[]
        pos=[]
        a =[]
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        # arr.claar()
        i=0
        j=0
        while i<len(pos) or j<len(neg):
            if i<len(pos):
                a.append(pos[i])
                i+=1
            if j<len(neg):
                a.append(neg[j])
                j+=1
        return a


if __name__ =='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.AlternatePositiveNegative(arr,n)
    print(result)