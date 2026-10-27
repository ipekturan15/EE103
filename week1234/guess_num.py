from secret_number import secret
#  infinite loop until the user guesses the secret number
# x = int(input("Guess the secret number: "))

# if x == secret:
#     print(" Your guess is same as the secret number.")
# elif x < secret:
#     print("Your guess is lower than the secret number.")
# elif x> secret:
#     print("Your guess is higher than the secret number.")

# while x < secret or x > secret:
#     x = int(input("Guess the secret number: "))
#     if x == secret:
#         print(" Your guess is same as the secret number.")
#     elif x < secret:
#         print("Your guess is lower than the secret number.")    
#     elif x> secret:
#         print("Your guess is higher than the secret number.")   

# after 5 wrong guess it prints and continious to ask guess still
# guess_count = 0 
# x = int(input("Guess the secret number: ")) 
# guess_count = guess_count + 1
# if x == secret:
#     print(" Your guess is same as the secret number.")
# elif x < secret:
#     print("Your guess is lower than the secret number.")
# elif x> secret:
#     print("Your guess is higher than the secret number.")

# while x < secret or x > secret:
#     x = int(input("Guess the secret number: "))
#     guess_count += 1
#     if x == secret:
#         print(" Your guess is same as the secret number.")
#     elif x < secret:
#         print("Your guess is lower than the secret number.")    
#     elif x> secret:
#         print("Your guess is higher than the secret number.")  
#     if guess_count >= 5:
#          print("Oh! Noooooo…") 
 
guess_count = 0 
x = int(input("Guess the secret number: ")) 
guess_count = guess_count + 1
if x == secret:
    print(" Your guess is same as the secret number.")
elif x < secret:
    print("Your guess is lower than the secret number.")
elif x> secret:
    print("Your guess is higher than the secret number.")

while x < secret or x > secret:
    x = int(input("Guess the secret number: "))
    guess_count += 1
    if x == secret:
        print(" Your guess is same as the secret number.")
    elif x < secret:
        print("Your guess is lower than the secret number.")    
    elif x> secret:
        print("Your guess is higher than the secret number.") 
    if guess_count >= 5:
        break
    

while guess_count >= 5 and x != secret :
    print("Oh! Noooooo…") 
    
# break ve while = true ile de yapılabilir 


  