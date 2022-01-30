from typing import Counter


class Solution:
    def LongestConsecutiveSubsequence(self,a,n):
        temp_arr = []
        count =0
        ans = []
        for i in range(1,n+1):
            temp_arr.append(i)
        print(temp_arr)
        for i in range(n):
            if a[i] in temp_arr:
                ans.append(a[i])
            else:
                i+=1
        print(ans)
        return count

if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    obj  = Solution()
    result = obj.LongestConsecutiveSubsequence(arr,n)
    print(result)