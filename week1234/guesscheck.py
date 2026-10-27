# given_number = 16

# guess = int(input("Guess a number: "))

# if guess**2 == given_number:
#     print("Your guess is square root of the" ,given_number, "!")

# else:
#     print("Your guess is not square root of the" ,given_number, "!")
    
# while guess**2 != given_number:
#     guess = int(input("Guess a number: "))
#     if guess**2 == given_number:
#      print("Your guess is square root of the" ,given_number, "!")
    
#     else:
#      print("Your guess is not square root of the" ,given_number, "!")

     
# given_number = 16

# guess = int(input("Guess a number: "))

# while guess ** 2 != given_number:
#     print("Your guess is not square root of the", given_number, "!")
#     guess = int(input("Guess a number: "))

# print("Your guess is square root of the", given_number, "!")

# given_number = int(input("Enter a number: "))

# while given_number < 0:
#     print(f'Square root of negative numbers is not a real number.')
#     given_number = int(input("Enter a number: "))

# guess = 1

# while guess ** 2 != given_number:
#     guess += 1 
#     if guess**2 > given_number:
#         print(f'{given_number} is not a perfect square')
#         break

# if guess ** 2 == given_number:
#     print("The square root of", given_number, "is", guess)


# enter = int(input("Enter a integer number: "))

# print(f' The cube of {enter} is {enter**3}')

enter = int(input("Enter a integer number: "))
guess = 0
while guess ** 3 < abs(enter):
    guess += 1

if guess ** 3 == abs(enter):
    if enter < 0:
        guess = -guess
    print("The cube root of", enter, "is", guess)
else:
    print(enter, "is not a perfect cube")