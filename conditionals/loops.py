# # 1. Print numbers from 1 to 10 using a loop.


# for i in range(1,11,1):
#     print(i)


# # 2.Print numbers from 10 to 1 in reverse order using a for loop.
# for i in range(10,0,-1):
#     print(i)

# # 3.Print all even numbers from 1 to 20.

# for i in range(1,21,1):
#     if i%2==0:
#           print(i)


# # 4.Print all odd numbers from 1 to 15.
# for i in range(1,21,1):
#     if i%2!=0:
#           print(i)


# # 4. Calculate the sum of numbers from 1 to 100.
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)


# # 5. Print the multiplication table of 5 (from 5×1 to 5×10).
# for i in range(1,10,1):
#     print( "5 x", i ,"=" ,5*i)

# # 6. Print all numbers divisible by 3 up to 50.
# num=3
# for i in range(1,51):
#     if i%num==0:
#         print(i,end=" ")


# # 7. Calculate the factorial of a number using a loop.
# n=int(input())
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# # 8.Reverse the digits of a number using a loop.
# n=int(input())
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(rev)


# # 9. Print squares of numbers from 1 to 10.
# for i in range(1,11):
#     print(i**2)

# # 10. Count the number of digits in an integer.
# count=0
# n=int(input("no :"))
# while n!=0:
#     n//=10
#     count+=1
# print(count)

# # 11. Find the sum of digits of a number.
# total=0
# n=int(input())
# while n!=0:
#     ld=n%10
#     total=total+ld
#     n//=10 
# print(total)

# # 12. Print powers of 2 up to 2^10.
# for i in range(1,11):
#     print("2^", i," = ",2**i)


# # 13. Check if a number is prime using a loop.
# n = int(input("Enter a number: "))
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         count = count + 1
# if count == 2:
#     print("Prime number")
# else:
#     print("Not a prime number")

# # 14. Print first 10 natural numbers using while loop.
# n=1
# while n<11:
#     print(n,end=" ")
#     n+=1

# # 15. Count down from 10 to 1 using a loop.
# count=0
# for i in range(1,10):
#     count+=1
# print(count)

# # 16. Find product of all numbers from 1 to 10.
# product=1
# for i in range(1,11):
#     product*=i
#     print(product)

# # 17. Print numbers from 1 to 100 in steps of 5.
# for i in range(1,101,5):
#     print(i)
    
# # 18. Find numbers between 1–50 divisible by both 3 and 5.
# a=3
# b=5
# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print(i)

# # 19. Print all prime numbers between 1 to 50.
# for num in range(2, 51):  # check numbers from 2 to 50
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num)

# # 20. Display the reverse of an integer.
# num=int(input())
# rev=0
# while num!=0:
#     ld=num%10     # get last digit
#     rev=rev*10+ld   # build reversed number
#     num//=10         # remove last digit
# print(rev)


# # 21. Find the smallest digit in a number.
# n=int(input())
# min_val=9
# while n>0:
#     ld=n%10
#     if ld<min_val:
#         min_val=ld
#     n//=10
# print("smallest number is ",min_val)

# # 22. Find the largest digit in a number.
# n=int(input("Enter a number :"))
# max=0
# while n>0:
#     ld=n%10
#     if ld > max:
#         max=ld
#     n//=10
# print("largest value is ",max)

# # 23. Print pattern: 1 2 3, 4 5 6, 7 8 9
# #  1 2 3 
# #  4 5 6 
# #  7 8 9

# count=1
# for i in range(3):
#     res=" "
#     for j in range(3):
#         res+=str(count)+" "
#         count+=1
#     print(res)

# # 24. Print pattern of stars in triangle format.
# # *
# # * *
# # * * * 
# # * * * * 
# # * * * * *
# rows=5
# for i in range(1,rows+1):
#     res=" "
#     for j in range(i):
#         res+="* "
#     print(res)

# # 25. Print sum of even digits in a number.
# rows=5
# num=2
# for i in range(1,rows+1):
#     res=" "
#     for j in range(i):
#         res+=str(num)+" "
#         num+=2
#     print(res)

# # 26. Print sum of odd digits in a number.
# rows=5
# num=1
# for i in range(1,rows+1):
#     res=" "
#     for j in range(i):
#         res+=str(num)+" "
#         num+=2
#     print(res)

# # 27. Print table of a given number.
# num=int(input())
# for i in range(1,11):
#     print(num," X ",i," = ",num*i)

# # 28. Count how many times a digit occurs in a number.
# count=0
# n=int(input())
# while n!=0:
#     last_digit=n%10
#     count+=1
#     n//=10
# print(count)

# # 29. Sum of squares of digits of a number.
# total=0
# n=int(input("Enter a number : "))
# while n!=0:
#     last_digit=n%10
#     s=last_digit**2
#     total+=s
#     n//=10
# print(total)

# # 30. Sum of cubes of digits of a number.
# total=0
# n=int(input("Enter a number : "))
# while n!=0:
#     last_digit=n%10
#     s=last_digit**3
#     total+=s
#     n//=10
# print(total)

# # 31. Count multiples of 3 between 1 and 100.
# count=0
# for i in range(1,101):
#     if i%3==0:
#         count+=1
# print(count)

# # 32. Print 10, 20, 30... up to 100.
# for i in range(1,101):
#     if i%10==0:
#         print(i,end=" ")

# # 33. Print reverse of a number using while loop.
# rev=0
# n=int(input("enter a number : "))
# while n!=0:
#     last=n%10
#     rev=rev*10+last
#     n//=10
# print(rev)

# # 34. Find if number is Armstrong number (3-digit only).
# # sum of digits when they raised to the power of no of digits is equal to orginal number 
# # ex --> 153 = 1^3+5^3+3^3=1+125+27 = 153
# total=0
# for i in range(100,1000):
#     total=0
#     num=i
#     while num!=0:
#         last = num%10
#         s=last**3
#         total+=s
#         num//=10
#     if total==i:
#         print(total)

# # 35. Print Fibonacci series up to n terms.
# # fibonacci sereies it is the sum of preceding ones
# # n1=0,n2=1,n1+n2,......nth terms
# n=int(input("Enter how may sereis you want : "))
# n1=0
# n2=1

# for i in range(n+1):
#     print(n1,end=" ")
#     c=n1+n2
#     n1=n2
#     n2=c

# # 36. Display all even digits in a number.
# n=int(input("Enter a Number : "))
# while n!=0:
#     last=n%10
#     if last%2==0:
#         print(last,end=" ")
#     n//=10

# # 37. Display all odd digits in a number.
# n=int(input("Enter a Number : "))
# while n!=0:
#     last=n%10
#     if last%2!=0:
#         print(last,end=" ")
#     n//=10


# # 38. Check if a number is palindrome using loop.
# # A palindrome number is a number that remains the same when its digits are reversed. 
# # For example, 121, 1331, and 4554 are palindrome numbers,madam,amma etc
# n=int(input("enter a number : "))
# rev=0
# while n!=0:
#     last =n%10
#     rev=rev*10+last
#     n//=10
# print(rev)


# # 39. Display the sum of factorials from 1 to 5.
# fact=1
# total=0
# for i in range(1,6):
#     fact*=i
#     total+=fact
# print(total)

# # 40. Print all factors of a number.
# n=int(input("Enter a Number : "))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i,end=" ")


# 41. Check if a number is perfect number using loop.
# sum of the factors of given number and excluding that number =given number then it is perfect number
n=6
total=0
for i in range(1,6):
    if n%i==0:
        total+=i
print(total)

# 42. Find the count of digits divisible by 3.
n=int(input("Enter a number : "))
count=0
while n!=0:
    last=n%10
    if last%3==0:
        count+=1
    n//=10
print(count)

# 43. Count the number of trailing zeroes in a factorial.
fact=1
count=0
for i in range(1,6):
    fact*=i
while fact%10==0:
        count+=1
        fact//=10
        print(count)

# 44. Print pattern: 1, 12, 123, ... up to n lines.
# 1
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 
for i in range(1,6):
    res=" "
    for j in range(1,i+1):
        res+=str(j)+" "
        
    print(res)


# Date : june 29th




# 45. Print pattern
# *       *
# *       *
# * * * * *
# *       *
# *       *
rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if j==1 or j==rows or i==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# 46. Print pattern
# * * * * *
#     *
#     *
#     *
#     *
rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if i==1 or j==(rows//2)+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# 47. Print pattern
# *       * 
# * *     *
# *   *   *
# *     * *
# *       *
rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if j==1 or i==j or j==rows:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)


# 48.print pattern 
# * * * * * 
#       *
#     *
#   *
# * * * * * 
rows=5
for i in range(1,rows+1):
    res=" "
    for j in range(1,rows+1):
        if i==1 or i+j==(rows+1) or i==rows:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
  
    







#   STRINGS

# Date :july 1st

# 49.write a function print characters from a given string whose index positions are divisible by a given number,
# excluding spaces. 
def char_in_index(string,number):
    for i in range(len(string)):
        char=string[i]
        if i%number==0 and char!=" ":
            print(char,i)

char_in_index("Be in your way",4)  
  
# 50.write a function  to count the number of uppercase and lowercase letters in a given string 
# (excluding spaces).
def upper_lower_count(string):
    upper_count=0
    lower_count=0
    for i in range(len(string)):
        if string[i]==string[i].upper() and string[i]!=" ":
            upper_count+=1
        elif string[i]==string[i].lower() and string[i]!=" ":
            lower_count+=1
    print(upper_count)
    print(lower_count)

upper_lower_count("ENJOY your Day")

# Date :july 2nd


# 51.Create a string with your name and print it.

myself="Chanamala Someswari"
print("My Name is:",myself)

# 52.Get the first character from the string.
print("First character:",myself[0])

# 53.Get the last character from the string.
last=len(myself)-1 #len-1 gives final index of string
print("Last Character",myself[last])

# 54.Concatenate two strings.
new="from Andhra"
print(myself+" "+new)

# 55. Repeat a string 3 times
for i in range(1,4):
    print(myself)

# 56. Slice the first 5 characters.

print(myself[0:5]) # stop before 5 0,1,2,3,4


# 57.Reverse a string using slicing.
print("string after slicing",myself[::-1])

# 58.Check if a substring exists in a string.
m2="eswari"  
if m2 in myself:
    print("string is exist")
else:
    print("string not exist")



# 59.Find the length of a string.
print("length of string:",len(myself))

# 60.Convert string to uppercase.
print(myself.upper())

# 61. Convert string to lowercase.
print(myself.lower())

# 62. Capitalize the first letter.
print("Captilize:",myself.capitalize())


# 63.Convert a string to title case.
print("title-case:",myself.title())

# 64.Remove leading spaces using lstrip().
word="           MORNING"
print("string after using lstrip:",word.lstrip())

# 65.Remove trailing spaces using rstrip().

w1="EVENING                                                      "

print("string without trailing spaces is:",w1.rstrip())




# Date : july 3rd


# 66.Check whether the char is lower,upper,number using function 

def char(string):
    ascii=ord(string)
    if ascii>=65 and ascii<=90:
        print("Character is in Uppercase : ",string)
    elif ascii>=97 and ascii<=122:
        print("character is in Lowercase : ",string)
    elif ascii>=48 and ascii<=57:
        print("it is a number")
    else:
        print("It's not a number, upper or lower case letter")
char("9")




# 67.convert hello-hfllp write function to convert vowel char into next character
def convert(str):
    str="hello"
    str2=" "
    for i in range(len(str)):
        value=ord(str[i])
        if str[i]=="a" or str[i]=="e" or str[i]=='i' or str[i]=='o' or str[i]=='u':
            char=chr(value+1 )
            str2+=char
        else:
              str2+=str[i]
    print(str2)  
convert("hello")
