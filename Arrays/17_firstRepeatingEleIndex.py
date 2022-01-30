class Solution:
    def firstRepeatingEleIndex(self,a,n):
        dic ={}
        index =1
        for ele in a:
            if ele not in dic:
                dic[ele] = 1
            else:
                dic[ele]= dic[ele] +1
        print(dic)
        # if len(dic) == 0:
        #     return -1
        # else:
        #     for i in range(n):
        #         if arr[i] == dic[0] :
        #             print(arr[i])
        #             return i
        for i in a:
            if dic[i] > 1:
                return index
            index+=1
        return -1


if __name__=='__main__':
    n  = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.firstRepeatingEleIndex(arr,n)
    print(result)