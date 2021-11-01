def comparison():
    a = 0
    b = 0
    with open("input","r") as f, open("output","w") as fo:
        r = f.read()
        n = r.split('\n')
        for i in n:
            j = i.split(' ')
            a += int(j[0])
            b += int(j[1])

        if 0<=a<=100 and 0<=b<=100:
            if a>b:
                fo.write("1")
            elif a<b:
                fo.write("2")
            else:
                fo.write("DRAW")
        else:
            print("Index out of range")

comparison()


a = input().split(" ")
b = input().split(" ")
_a = 0
_b = 0

for i in range(len(a)):
    _a += int(a[i])
    _b += int(b[i])

if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print("DRAW")

a1 = int(input(
))
b1 = int(input())
a2 = int(input())
b2 = int(input())
a3 = int(input())
b3 = int(input())
a4 = int(input())
b4 = int(input())

a = a1 + a2 + a3 + a4
b = b1 + b2 + b3 + b4

if a > b:
    print(1)
elif a < b:
    print(2)
else:
    print("DRAW")
