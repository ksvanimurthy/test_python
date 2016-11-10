class ClassObjects:
    dangerous = 2

c1 = ClassObjects()
c2 = ClassObjects()

print(c1.dangerous)     # 2

c1.dangerous = 3
print(c1.dangerous)     # 3
print(c2.dangerous)     # 2

del c1.dangerous
print(c1.dangerous)     # Error

ClassObjects.dangerous = 3
print(c2.dangerous)     # 3

