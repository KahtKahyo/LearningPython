import math
import random

print("5 + 2 = ", 5 + 2)
print("5 - 2 = ", 5 - 2)
print("5 * 2 = ", 5 * 2)
print("5 / 2 = ", 5 / 2)
print("5 // 2 = ", 5 // 2)
print("5 % 2 = ", 5 % 2)
print("5 ** 2 = ", 5**2)

# shorcut equation
# add 1
i = 2
i += 1
print("i = ", i)

# Math Functions
print("abs(-1) ", abs(-1))
print("max(5, 4) ", max(5, 4))
print("min(5, 4) ", min(5, 4))
print("pow(2, 2) ", pow(2, 2))
print("ceil(4.5) ", math.ceil(4.5))
print("floor(4.5) ", math.floor(4.5))
print("round(4.5) ", round(4.5))
print("exp(1) ", math.exp(1))  # e**x
print("log(e) ", math.log(math.exp(1)))
print("log(100) ", math.log(100, 10))  # Base 10 Log
print("sqrt(100) ", math.sqrt(100))
print("sin(0) ", math.sin(0))
print("cos(0) ", math.cos(0))
print("tan(0) ", math.tan(0))
print("asin(0) ", math.asin(0))
print("acos(0) ", math.acos(0))
print("atan(0) ", math.atan(0))
print("sinh(0) ", math.sinh(0))
print("cosh(0) ", math.cosh(0))
print("tanh(0) ", math.tanh(0))
print("asinh(0) ", math.asinh(0))
print("acosh(pi) ", math.acosh(math.pi))
print("atanh(0) ", math.atanh(0))
print("hypot(0) ", math.hypot(10, 10))  # sqrt(x*x + y*y)
print("radians(0) ", math.radians(0))
print("degrees(pi) ", math.degrees(math.pi))

# Random
print("Random Integer: ", random.randint(1, 101))

# Infinity
print("Infinity: ", math.inf)

# Is infinity greater than 0?
print("Is infinity greater than 0? ", math.inf > 0)

# Subtract infinity with infinity which resulted in nan
print("infinity - Infinity: ", math.inf - math.inf)
