num1 = int(input("Enter the first number\n"))
num2 = int(input("Enter the second number\n"))
if num1 > num2:
    min = num1
else:
    min = num2
for i in range(1, min+1):
    if(num1 % i == 0 and num2 % i == 0):
        hcf = i
print(f"The HCF of these two numbers is {hcf}")