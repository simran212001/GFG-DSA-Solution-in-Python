class Solution:
    def SortArray(self,arr,N):
        # return arr.sort()
# Method 2
        count_zero = 0
        count_one = 0
        count_two = 0
        for i in range(N):
            if arr[i] == 0:
                count_zero +=1
            elif arr[i] == 1:
                count_one+=1
            else:
                count_two+=1
        new_arr = count_zero*[0] + count_one*[1]+ count_two*[2]
        return new_arr


if __name__=='__main__':
    N= int(input())
    arr = list(map(int,input().split()))
    obj = Solution()
    result =obj.SortArray(arr ,N)
    for i in result:
        print(i,end=' ')
    