class Solution:
    def Factorial(self,n):
        fact = 1
        for i in range(1,n+1):
            fact = fact*i
        return fact

if __name__ =='__main__':
    n = int(input())
    obj = Solution()
    result = obj.Factorial(n)
    print(result)