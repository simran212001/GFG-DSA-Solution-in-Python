class Solution:
    def Duplicate(self,arr,N):
        
        dic = {}
        ls = []
        print(dic)
        for el in arr:
            if el not in dic:
                dic[el] = 1
                # print(dic)
                # print(dic[el])
            else:
                dic[el] += 1
                # print(dic)
                if(dic[el] == 2):
                    ls.append(el)
                
        if(len(ls) == 0):
            return [-1]
        ls.sort()
        return ls

if __name__=='__main__':
    N = int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.Duplicate(arr,N)
    for i in result:
        print(i,end=' ')

