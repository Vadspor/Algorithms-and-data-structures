import random
import time
import timeit
from math import *
# a = [random.randint(0, 100) for i in range(10)]
a = [60, 16, 41, 6, 59, 79, 34, 15]
b = a.copy()
c = a.copy()
c1 = a.copy()

# c = [60, 16, 41, 6, 59, 79, 34, 15]
# x = [i for i in range(8, 0, -4)]
# print(x)
# y = [i for i in range(8, 0, -2)]
# print(y)

# ck = 0
# cm = 0
# ct = 0
# print(a)

a1 = sorted(b)
print(f"Sorted list is: {a1}")
print(f"Dont sorted list: {b}\n")


def ComparisonSortList(a):
    true = []
    b = sorted(a)
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] == b[i]:
                true.append(True)
            else:
                true.append(False)
        if False in true:
            return False, true
        else:
            return True
    else:
        return False, true
    


def InsertSort1(a):
    ck = 0
    cm = 0
    ct = time.time()
    for i in range(1, len(a)):
        # if a[i] > a[i-1]:
        #     continue
        for j in range(i):
            ck += 1
            if a[i] < a[j]:
                cm += 1
                # print(i+1, j+1)
                a.insert(j, a[i])
                # print(a)
                if i > j:
                    a.pop(i+1)
                else:
                    a.pop(i)
                # print(a)
                break
    ctt = time.time() - ct
    # print(f"Insert sort compares: {ck}")
    # print(f"Insert sort movies: {cm}")
    # print(f"Insert sort time: {ctt}")
    return a, ck, cm, ctt


# print("\n\nTesting Insert sort:")
#
# print("\nInsert sort a")
# insoo = InsertSort1(a)
# print(insoo[0])
# print(f"Insert sort compares: {insoo[1]}")
# print(f"Insert sort movies: {insoo[2]}")
# print(f"Insert sort time: {insoo[3]}")
# print(ComparisonSortList(a))

# print(timeit.timeit("InsertSort1(a)", "from __main__ import InsertSort1, a", number=100))



def ShellSort1(c):
    ck = 0
    cm = 0
    ct = time.time()
    z = len(c)
    while z > 0:
        z = z // 2
        for i in range(len(c)):
            for j in range(z, len(c)):
                ck += 1
                if c[j-z] > c[j]:
                    cm += 1
                    # print(f"j: {j + 1}  j+z: {j + 1 + z}  z: {z}")
                    c[j-z], c[j] = c[j], c[j-z]
                    # cn = c[j]
                    # c[j] = c[j - z]
                    # c[j - z] = cn
                    # print(c)
    ctt = time.time() - ct
    return c, ck, cm, ctt

# print(ShellSort1(c))
# print(ComparisonSortList(c), "\n")

def buble(a):
    ck = 0
    cm = 0
    ct = time.time()
    for i in range(len(a)):
        for j in range(1, len(a)):
            ck += 1
            if a[j-1] > a[j]:
                cm += 1
                an = a[j]
                a[j] = a[j-1]
                a[j-1] = an
    ctt = time.time() - ct
    # print(f"Buble sort compares: {ck}")
    # print(f"Buble sort movies: {cm}")
    # print(f"Buble sort time: {ctt}")
    return a, ck, cm, ctt

# print(buble(c1))
# print(ComparisonSortList(c1), "\n")


def ShellSort2(c):
    ck = 0
    cm = 0
    ct = 0
    z = len(c)
    for x in range(len(c)):
        z = z // 2
        if z == 0:
            break
        for q in range(z):
            exec(f"l_{z}_{q} = []")

        for f in range(len(c)):
            exec(f"l_{z}_{f%z}.append(c[f])")

        for g in range(z):
            # print(c)
            # exec(f'print(l_{z}_{g}, "l_{z}_{g}")')
            # exec(f"InsertSort1(l_{z}_{g})")
            inso = InsertSort1(locals()[f"l_{z}_{g}"])
            ck += inso[1]
            cm += inso[2]
            ct += inso[3]
            # print("\n")
            # print(c)
            # exec(f'print(l_{z}_{g}, "l_{z}_{g}")')
            for h in range(g, len(c), z):
                # print(f"h: {h} g: {g} z: {z}")
                # exec(f"print(h%len(l_{z}_{g}))")
                exec(f"c[h] = l_{z}_{g}[h//z]")
                # print(c)
    return c, ck, cm, ct


# print(ShellSort2(c1))
# print(ComparisonSortList(c1))



def InsertSort2(a):
    ck = 0
    cm = 0
    ct = time.time()
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            ck += 1
            if a[j] < a[j-1]:
                cm += 1
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break
    ctt = time.time() - ct
    return a, ck, cm, ctt


# print(c1)
# print(InsertSort2(c1))
# print(ComparisonSortList(c1))


def ShellSort3(c):
    ck = 0
    cm = 0
    ct = time.time()
    n = len(c)
    hk = [1]
    for i in range(n):
        hhk = 3*hk[0] + 1
        if hhk > n//2:
            break
        hk.insert(0, hhk)
    print(hk)
    for x in range(len(hk)):
        z = hk[x]
        for i in range(1, n):
            for j in range(i, 0, -z):
                ck += 1
                if c[j] < c[j-z]:
                    cm += 1
                    c[j], c[j-z] = c[j-z], c[j]
                else:
                    break
    ctt = time.time() - ct
    return c, ck, cm, ctt


# print(c1)
# print(ShellSort3(c1))
# print(ComparisonSortList(c1))



a100 = [random.randint(0, 200) for p in range(100)]
a1000 = [random.randint(0, 2000) for o in range(1000)]
a10000 = [random.randint(0, 20000) for k in range(10000)]
b100 = a100.copy()
b1000 = a1000.copy()
b10000 = a10000.copy()
c100 = a100.copy()
c1000 = a1000.copy()
c10000 = a10000.copy()
c1100 = a100.copy()
c11000 = a1000.copy()
c110000 = a10000.copy()
s100 = a100.copy()
s1000 = a1000.copy()
s10000 = a10000.copy()
sh100 = a100.copy()
sh1000 = a1000.copy()
sh10000 = a10000.copy()
iso100 = a100.copy()
iso1000 = a1000.copy()
iso10000 = a10000.copy()

print("\n\nTesting Insert sort 1:")

print("\nInsert sort 1 a100")
inso11 = InsertSort1(a100)
print(inso11[0])
print(f"Insert sort 1 compares: {inso11[1]}")
print(f"Insert sort 1 movies: {inso11[2]}")
print(f"Insert sort 1 time: {inso11[3]}")
print(ComparisonSortList(a100))

print("\nInsert sort 1 a1000")
inso12 = InsertSort1(a1000)
print(inso12[0])
print(f"Insert sort 1 compares: {inso12[1]}")
print(f"Insert sort 1 movies: {inso12[2]}")
print(f"Insert sort 1 time: {inso12[3]}")
print(ComparisonSortList(a1000))

print("\nInsert sort 1 a10000")
inso13 = InsertSort1(a10000)
print(inso13[0])
print(f"Insert sort 1 compares: {inso13[1]}")
print(f"Insert sort 1 movies: {inso13[2]}")
print(f"Insert sort 1 time: {inso13[3]}")
print(ComparisonSortList(a10000))


print("\n\nTesting Shellsort2:")

print("\nShellsort2 a100")
shso1 = ShellSort2(c1100)
print(shso1[0])
print(f"Shellsort2 compares: {shso1[1]}")
print(f"Shellsort2 movies: {shso1[2]}")
print(f"Shellsort2 time: {shso1[3]}")
print(ComparisonSortList(c1100))

print("\nShellsort2 a1000")
shso2 = ShellSort2(c11000)
print(shso2[0])
print(f"Shellsort2 compares: {shso2[1]}")
print(f"Shellsort2 movies: {shso2[2]}")
print(f"Shellsort2 time: {shso2[3]}")
print(ComparisonSortList(c11000))

print("\nShellsort2 a10000")
shso3 = ShellSort2(c110000)
print(shso3[0])
print(f"Shellsort2 compares: {shso3[1]}")
print(f"Shellsort2 movies: {shso3[2]}")
print(f"Shellsort2 time: {shso3[3]}")
print(ComparisonSortList(c110000))


print("\n\nTesting Insert sort 2:")

print("\nInsert sort 2 a100")
inso21 = InsertSort2(iso100)
print(inso21[0])
print(f"Insert sort 2 compares: {inso21[1]}")
print(f"Insert sort 2 movies: {inso21[2]}")
print(f"Insert sort 2 time: {inso21[3]}")
print(ComparisonSortList(iso100))

print("\nInsert sort 2 a1000")
inso22 = InsertSort2(iso1000)
print(inso22[0])
print(f"Insert sort 2 compares: {inso22[1]}")
print(f"Insert sort 2 movies: {inso22[2]}")
print(f"Insert sort 2 time: {inso22[3]}")
print(ComparisonSortList(iso1000))

print("\nInsert sort 2 a10000")
inso23 = InsertSort2(iso10000)
print(inso23[0])
print(f"Insert sort 2 compares: {inso23[1]}")
print(f"Insert sort 2 movies: {inso23[2]}")
print(f"Insert sort 2 time: {inso23[3]}")
print(ComparisonSortList(iso10000))


print("\n\nTesting Shellsort3:")

print("\nShellsort3 a100")
shso31 = ShellSort3(sh100)
print(shso31[0])
print(f"Shellsort3 compares: {shso31[1]}")
print(f"Shellsort3 movies: {shso31[2]}")
print(f"Shellsort3 time: {shso31[3]}")
print(ComparisonSortList(sh100))

print("\nShellsort3 a1000")
shso32 = ShellSort3(sh1000)
print(shso32[0])
print(f"Shellsort3 compares: {shso32[1]}")
print(f"Shellsort3 movies: {shso32[2]}")
print(f"Shellsort3 time: {shso32[3]}")
print(ComparisonSortList(sh1000))

print("\nShellsort3 a10000")
shso33 = ShellSort3(sh10000)
print(shso33[0])
print(f"Shellsort3 compares: {shso33[1]}")
print(f"Shellsort3 movies: {shso33[2]}")
print(f"Shellsort3 time: {shso33[3]}")
print(ComparisonSortList(sh10000))


print("\n\nTesting Buble sort:")

print("\nBuble sort a100")
buso1 = buble(b100)
print(buso1[0])
print(f"Buble sort compares: {buso1[1]}")
print(f"Buble sort movies: {buso1[2]}")
print(f"Buble sort time: {buso1[3]}")
print(ComparisonSortList(b100))

print("\nBuble sort a1000")
buso2 = buble(b1000)
print(buso2[0])
print(f"Buble sort compares: {buso2[1]}")
print(f"Buble sort movies: {buso2[2]}")
print(f"Buble sort time: {buso2[3]}")
print(ComparisonSortList(b1000))

print("\nBuble sort a10000")
buso3 = buble(b10000)
print(buso3[0])
print(f"Buble sort compares: {buso3[1]}")
print(f"Buble sort movies: {buso3[2]}")
print(f"Buble sort time: {buso3[3]}")
print(ComparisonSortList(b10000))


print("\n\nTesting Shellsort1:")

print("\nShellsort1 a100")
shso1 = ShellSort1(c100)
print(shso1[0])
print(f"Shellsort1 compares: {shso1[1]}")
print(f"Shellsort1 movies: {shso1[2]}")
print(f"Shellsort1 time: {shso1[3]}")
print(ComparisonSortList(c100))

print("\nShellsort1 a1000")
shso2 = ShellSort1(c1000)
print(shso2[0])
print(f"Shellsort1 compares: {shso2[1]}")
print(f"Shellsort1 movies: {shso2[2]}")
print(f"Shellsort1 time: {shso2[3]}")
print(ComparisonSortList(c1000))

print("\nShellsort1 a10000")
shso3 = ShellSort1(c10000)
print(shso3[0])
print(f"Shellsort1 compares: {shso3[1]}")
print(f"Shellsort1 movies: {shso3[2]}")
print(f"Shellsort1 time: {shso3[3]}")
print(ComparisonSortList(c10000))


print("\n\nTesting Python sort:")

print("\nPython sort a100")
start = time.time()
s100.sort()
end = time.time()
print(s100)
print(f"Sort time: {end - start}")

print("\nPython sort a1000")
start = time.time()
s1000.sort()
end = time.time()
print(s1000)
print(f"Sort time: {end - start}")

print("\nPython sort a10000")
start = time.time()
s10000.sort()
end = time.time()
print(s10000)
print(f"Sort time: {end - start}")


# print(timeit.timeit("ShellSort2(a100)", "from __main__ import ShellSort2, a100", number=100))
# print(timeit.timeit("ShellSort2(a1000)", "from __main__ import ShellSort2, a1000", number=100))
# print(timeit.timeit("ShellSort2(a10000)", "from __main__ import ShellSort2, a10000", number=100))



