x = int(input("Give me a number: "))
result = 0
for i in range(x + 1):
    result += i
print(f"The sum of numbers from 0 to {x} is {result}")

# i = 0
# while i <= x:
#     result += i
#     i += 1  
# print(f"The sum of numbers from 0 to {x} is {result}")

sum_gauss = int(x * (x + 1) / 2)
print(f"The sum of numbers from 0 to {x} is {sum_gauss}")


if result == sum_gauss:
    print("The two sums are equal.")
