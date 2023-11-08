# // factorial of nth number:

num = int(input("Enter the num: "))

fact = 1
for i in range(1,num+1):
    fact=fact*i
print(fact)