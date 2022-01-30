# def ReverseS(s):
#     # return s[::-1]
#     str = ""
#     for i in s:
#         str =  i+str
#     return str
# if __name__ == '__main__':
    
#     s = str(input())
#     print(ReverseS(s))


def reverseArray(a,n):
    
    B = list()
    for i in range(n-1 ,-1,-1):
        B.append(a[i])
    return B
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(reverseArray(arr,n))
    
    