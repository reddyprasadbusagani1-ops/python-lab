a = 10
b = 3

print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)

print("\nRelational Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\nAssignment Operators")
x = 10
print("x =", x)

x += 5
print("x += 5 :", x)

x -= 3
print("x -= 3 :", x)

x *= 2
print("x *= 2 :", x)

x /= 2
print("x /= 2 :", x)

x %= 3
print("x %= 3 :", x)

print("\nLogical Operators")
print("a > 5 and b < 5 :", a > 5 and b < 5)
print("a > 5 or b > 5  :", a > 5 or b > 5)
print("not(a > 5)      :", not(a > 5))

print("\nBitwise Operators")
print("a & b  =", a & b)
print("a | b  =", a | b)
print("a ^ b  =", a ^ b)
print("~a     =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)

print("\nTernary Operator")
result = a if a > b else b
print("Greater number =", result)

print("\nMembership Operators")
lst = [1, 2, 3, 4, 5]
print("3 in list     :", 3 in lst)
print("10 not in list:", 10 not in lst)

print("\nIdentity Operators")
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print("x is y     :", x is y)
print("x is z     :", x is z)
print("x is not z :", x is not z)
