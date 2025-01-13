n = int(input("enter the values"))
count = 0
i = 0
while(i<=n):
    if (n % i == 0):
        count += 1
        i += 1
if(count  == 2):
        print("prime numbers")
else:
        print("composite numbers")