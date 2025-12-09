#Definition:--->The Fibonacci is a number sequence in mathematics where each number is the sum of the previous two numbers.

# Simple Python Program for Fibonacci Series

n = int(input("Enter how many terms: "))

a, b = 0, 1
print(a, b, end=" ")

for i in range(2, n):
    c = a + b
    print(c, end=" ")
    a = b
    b = c

# Fibonacci Sequence – Explanation Diagram
Start
   |
   v
  a = 0   (First term)
  b = 1   (Second term)
   |
   v
+-------------------------------+
|   Next term = a + b           |
+-------------------------------+
          |
          v
   c = a + b
          |
          v
  Print c
          |
          v
Update values:
   a = b
   b = c
          |
          
