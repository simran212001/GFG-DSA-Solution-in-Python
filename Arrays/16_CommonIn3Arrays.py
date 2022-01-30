class Solution:
    def CommonIn3Arrays(self,arr1,arr2,arr3,N1,N2,N3):
        list = []
        i ,j ,k = 0,0,0
        while (i<N1 and j<N2 and k<N3):
            if (arr1[i] == arr2[j] and arr2[j] == arr3[k]) and (arr1[i] not in list):
                list.append(arr1[i])
                i+=1
                j+=1
                k+=1
            elif arr1[i]<arr2[j]:
                i+=1
            elif arr2[j] < arr3[k]:
                j+=1
            else:
                k+=1
        return list

if __name__=='__main__':
    N1 = int(input())
    arr1 = list(map(int,input().split()))
    N2 =int(input()) 
    arr2 =list(map(int,input().split())) 
    N3 = int(input())
    arr3 = list(map(int,input().split()))
    obj = Solution()
    result = obj.CommonIn3Arrays(arr1,arr2,arr3,N1,N2,N3)
    if len(result) ==0:
         print(-1)
    else:
        for a in result:
            print(a,end=' ')