class Solution:
    def SubArray(self,arr,n,s):
        A =[]
        start = 0
        check_sum = arr[0]
        i = 1
        while i<=n:
            if check_sum > s:
                
                while check_sum >= s and start<i-1 :
                    if check_sum == s:
                        A.append(start+1)
                        A.append(i)
                        return A
                    check_sum = check_sum - arr[start]
                    start = start+1
                    
            if check_sum == s:
                A.append(start+1)
                A.append(i)
                return A
                
            if check_sum < s and i<n:
                check_sum = check_sum + arr[i]
            i+=1
        A.append(-1)
        return A
import math     

if __name__ == '__main__':
    N ,S = map(int,input().split())
    arr = list(map(int,input().split()))
    obj = Solution()
    result = obj.SubArray(arr,N,S)
    for ele in result:
        print(ele,end=' ')