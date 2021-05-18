# class Solution:
#     def Sum(self):
#         N = int(input())
#         c=0
#         if N<10**4:
#             for i in range(1,N+1):
#                 c+=i
#         else:
#             return "Index out of range !"
#
#         return c
#
# p = Solution()
# print(p.Sum())

class Solution:
    def Cheese(self):
        numbers = "12345678"
        symbols = "ABCDEFGH"
        mv = input("Enter your move: ")
        for i in range(len(mv)):
            if mv[i] in symbols or numbers:
                t = symbols.find(mv[3])
                num = int(mv[4])
                if mv[2] == '-' and mv[0] == symbols[t-1] or mv[0] == symbols[t+1]:
                    if num + 2 == int(mv[1]) or num - 2 == int(mv[1]):
                        print("YES")
                        break
                elif mv[2] == '-' and mv[0] == symbols[t-2] or mv[0] == symbols[t+2] :
                    if num + 1 == int(mv[1]) or num - 1 == int(mv[1]):
                        print("YES")
                        break
                else:
                    print("No")
                    break
            else:
                print("Error")
                break

p=Solution()
p.Cheese()
