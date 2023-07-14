## first 10 naural numbers

# i = 1
# while i<=10:
#     print(i)
#     i+=1

##sum of all numbers from 1 to a given number

# num = int(input("Enter the value : "))
# sum=0
# for i in range(1, num+1):
#     sum=sum+i
#     i=i+1
#     print("sum=",sum)

##print multiplication table of a given number
# n = int(input("enter the value: "))
# for i in range(1,21):
#     print(n,"*",i,"=",n*i)


##Display numbers from a list using loop
# n=input('enter the lists: ')
# for i in n:
#     print(i)


##Count the total number of digits in a number

# n = input("enter the digits: ")
# len_digit=len(n)
# print(len_digit)


##Print list in reverse order using a loop
# n=input("enter the list: ")
# for i in (n[::-1]):
#     print(i)

##numbers from -10 to -1 using for loop
# n= int(input("enter the num: "))
# for i in range((n-1),0,-1):
#     print(i)

##display all prime numbers within a range
n=int(input("enter the prime num: "))
for i in range(1,n+1):
    if i%2==0:
        print(i)
        

##if  else block ="Done" after  excution of code

# n=int(input("enter the str: "))
# for i in range(1,n+1):
#     if i<=10:
#         print(i)
#     else:
#         print("Done")

##Display Fibonacci series up to 10 terms

# a=0
# b=1
# for i in range(10):
#     c=a+b
#     a=b
#     b=c
#     print(c)