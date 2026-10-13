#  with for loop

# x = int(input("Give me a number: "))

# result = 1
# for i in range(1,x+1):
#     result *= i
# print(f'The factorial of {x} is {result}')


x = int(input("Give me a number: "))

result = 1
i = 1 
while i <= x:
    result *= i
    i += 1

print(f"The factorial of {x} is {result}")