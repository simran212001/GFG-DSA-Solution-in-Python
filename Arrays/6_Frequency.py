# Find the Frequency


def FrequencyOfX(arr,n,x):
    Count = 0
    for i in range(n):
        if arr[i] == x:
            Count+=1
    return Count
if __name__ == '__main__':
    t =  int(input())
    for _ in range(t):
        n= int(input())
        arr = list(map(int,input().split()))
        x = int(input())
        print(FrequencyOfX(arr,n,x))