# Kth smallest element 
def KthSmallest(a,n,k):
    a.sort()
    return a[k-1]

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        k = int(input())
        print(KthSmallest(arr,n,k))