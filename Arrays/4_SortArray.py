def SortedArray(a,n):
    return sorted(a)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(SortedArray(arr,n))