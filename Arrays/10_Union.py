
class Solution:
    def UnionOfArrays(self,a,b,n,m):
        arr = set(a+b)
        l = len(arr)
        return l
if __name__=='__main__':
    n ,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    obj = Solution()
    result =obj.UnionOfArrays(a,b,n,m)
    # for i in result:
    #     print(i ,end=' ')
    print(result)