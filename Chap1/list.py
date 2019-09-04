print("配列")
a = [1, 2, 3, 4, 5]
print(a)
print(len(a))
print(a[0])
print(a[4])
a[4] = 99
print(a[4])
print(a)
# --> [1, 2, 3, 4, 99]
print("配列のスライシング")
print(a[0:2])
# --> [1, 2]
print(a[1:])
# --> [2, 3, 4, 99]
print(a[:3])
# --> [1, 2, 3]
print(a[:-1])
# --> [1, 2, 3, 4]
print(a[:-2])
# --> [1, 2, 3]
print(a[-1:])
# --> [99]
print(a[-3:])
# --> [3, 4, 99]

