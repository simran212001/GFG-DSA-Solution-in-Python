from collections import defaultdict 

class Solution:
    def Non_Repeating(self,a,n):
        dic ={}
        list = []
        index =1
        for ele in a:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele] = dic[ele] + 1
        print(dic)
        for i in range(n):
            # print(dic[i])   = count of elements
            if dic[a[i]] == 1:
                return a[i]

        return -1

        
if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.Non_Repeating(arr,n)
    print(result)