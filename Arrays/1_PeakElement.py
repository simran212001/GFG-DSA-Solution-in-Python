# Peak element is the element which is greater than or equal to its neighbors. For example - 
# In Array {1,4,3,6,7,5}, 4 and 7 are peak elements. 
def PeakEle(a,n):
    # no of elements in the array is 1
    if n == 1:
        return 0
    # 1st and 2nd element
    if a[0] >= a[1]:
        return 0
    # last(n-1) and second last(n-2) elements
    if a[n-1] >= a[n-2]:            
        return 0
    # Now for other elements of the array
    for i in range(1,n):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            return 1
        else:
            return 0

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))
    print(PeakEle(array,n))    
