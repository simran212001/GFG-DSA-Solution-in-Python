


class Solution:
    def CountPairs(self,arr,N,K):
        dic = {}
        count =0
        for i in range(N):
            if (K-arr[i]) in dic:
                count+=dic[K-arr[i]]
                # print(dic[K-arr[i]])
            if arr[i] in dic:
                dic[arr[i]] +=1
                # print(dic[arr[i]])
            else:
                dic[arr[i]] = 1
        return count
                


if __name__ =='__main__':
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))

    obj = Solution()
    result = obj.CountPairs(arr,N,K)
    print(result)
