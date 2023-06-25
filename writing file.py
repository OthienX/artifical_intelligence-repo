#t= open("c:\\ users\\ david\\ documents\\ text.txt", "w")
#1/0
try:
    a= int(input("enter the first number"))
    b=int(input("enter the second number"))
    print(a/b)
except ZeroDivisionError:
    print("u have tried to divide by zero")
else:
    print("u didnt try to zero by zero well done")