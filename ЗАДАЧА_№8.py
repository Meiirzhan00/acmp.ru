class Solution:
    def Arithmetic(self):
        numbers = input().split(' ')
        A=int(numbers[0])
        B=int(numbers[1])
        C=int(numbers[2])
        if A and B <= 10**2 or C <= 10**6:
            if A * B == C:
                print("YES")
            else:
                print("NO")
        else:
            print("Index out of range!")

p = Solution()
p.Arithmetic()
