def LargestsumcontiguousSubarray(arr,n):
    sum =0
    for i in range(n):
        while arr[i] > 0:
            sum = sum+arr[i]
            i+=1
        while arr[i]<0:
            return max(arr[i])
    return sum

if __name__=='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(LargestsumcontiguousSubarray(arr,n))