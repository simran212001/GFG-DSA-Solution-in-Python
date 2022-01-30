
class Solution:    
    def quickSort(self,arr,start,end):
        if start < end:
            pivot = Solution.partition(self,arr,start,end)
            Solution.quickSort(self,arr,start,pivot-1)
            Solution.quickSort(self,arr,pivot+1,end)
        # rendeturn arr

    def partition(self,arr,start,end):
        i = start
        j = end-1
        pivot = arr[end]
        while i<j:
            while i<end and arr[i]<pivot:
                i+=1
            while j >start and arr[j] >=pivot:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        if arr[i] >pivot:
            arr[i],arr[end] = arr[end],arr[i]
        return i
    
if __name__=="__main__":
    N = int(input())
    arr = list(map(int,input().split()))
    start = 0
    end = N-1
    obj = Solution()
    obj.quickSort(arr,start,end)
    for i in arr:
        print(i,end=' ')