n=int(input("Enter the limit = "))
def add(n):
    sum=0
    for i in range(n):
        num=int(input("Enter the number to add = "))
        sum=sum+num
    print("The sum is =",sum)
add(n)    