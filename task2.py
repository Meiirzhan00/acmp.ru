class Solution:
    def task2(self):
        n=int(input())
        sum=0
        if n>0:
            sum = (n+1)*n/2
        else:
            sum = (n-1)*n/(-2)+1

        return int(sum)

p=Solution()
print(p.task2())
