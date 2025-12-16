# Right Angle Triangle Pattern:-->

for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()

# output:--->
*
* *
* * *
* * * *

# Inverted Right Angle Triangle:-->

for i in range(4, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
  # output:--->
* * * *
* * *
* *
*


#  Number Pattern (Increasing)

for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
  # output:-->
1
1 2
1 2 3
1 2 3 4

# Same Number Pattern:---->

for i in range(1, 5):
    for j in range(i):
        print(i, end=" ")
    print()

#output:--->
1
2 2
3 3 3
4 4 4 4

# Alphabet Pattern:---->

for i in range(1, 5):
    ch = 65
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()

# output:-->
A
A B
A B C
A B C D


# Diamond Pattern:---->

n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

#output:--->
  *
  * *
 * * *
  * *
   *





















