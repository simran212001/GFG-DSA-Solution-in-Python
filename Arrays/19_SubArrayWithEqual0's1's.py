def SubArrayWithEqual01(arr,n):
    dic = {}       
    sum = 0  
    for i in range(n):
        if arr[i] == 0:
            arr[i] = -1
        
        sum = sum+arr[i]
    

if __name__ =='__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(SubArrayWithEqual01(arr,n))