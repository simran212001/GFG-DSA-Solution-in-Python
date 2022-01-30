# A[] = {3, 2, 1, 56, 10000, 167}  1, 345, 234, 21, 56789

# def getMinMax(a,n):
#     Max = max(a)
#     Min = min(a)
#     return Max,Min

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         n = int(input())
#         arr = list(map(int,input().split()))
#     print(getMinMax(arr,n))
a,b,c = map(int,input().split())
max = max(a,b,c)
min = min(a,b,c)
if (a<max and a>min):
    print(a)
elif(b<max and b>min):
    print(b)
else:
    print(c)