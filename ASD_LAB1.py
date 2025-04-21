def pow(x, y):
    if y > 0:
        return pow(x, y-1)*x
    elif y == 0:
        return 1
    elif y < 0:
        return pow(x, y+1)/x
    else:
        return x

print(pow(3, 4))
print(pow(2, 0))
print(pow(25, -1))

def Evclide(x, y):
    # print(f'x: {x}')
    # print(f'y: {y}')
    if x % y != 0:
        return Evclide(y, x % y)
    else:
        return abs(y)

a = None
while a == None:
    try:
        a = int(input("Enter a number a: "))
    except ValueError:
        print("Invalid input. Please insert a integer")

b = None
while b == None:
    try:
        b = int(input("Enter a number b: "))
    except ValueError:
        print("Invalid input. Please insert a integer")

# print(f'a: {a}')
# print(f'b: {b}')

if a == 0:
    x, y = a, b
elif b == 0:
    x, y = b, a
elif a > b:
    x, y = a, b
else:
    x, y = b, a

print(Evclide(x, y))

k = []
def My_Tower(n, pot, dop, kin):
    if n > 0:
        My_Tower(n - 1, pot, kin, dop)
        print(f'from {pot} move {n} to {kin}')
        My_Tower(n - 1, dop, pot, kin)
        k.append(n)
My_Tower(5, "A", "B", "C")
print(len(k))


