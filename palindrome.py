# Explanation of Palindrome Number:---> A palindrome number is a number that remains the same when reversed.
Examples: 121, 1331, 5445, 909
#Explanation of Code:--->

num = int(input("Enter a number: "))
temp = num
rev = 0

while temp > 0:
    digit = temp % 10          # extract last digit
    rev = rev * 10 + digit     # build reversed number
    temp = temp // 10          # remove last digit

