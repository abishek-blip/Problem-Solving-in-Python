# swapping using temporary variable

num1 = 5
num2 = 3
temp = num1
num1 = num2
num2 = temp
print("Swapping using temporary variable:")
print("num1 = ", num1)
print("num2 = ", num2)

# swapping without using temporary variable

num1 = 10
num2 = 5
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Swapping without using temporary variable:")
print("num1 = ", num1)
print("num2 = ", num2)
