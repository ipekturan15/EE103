
# start = int(input("Başlangıç sayısı girin: "))
# finish = int(input("Bitiş sayısı girin: "))
# a = start
# results_for = 1
# result_while = 1

# for i in range(start, finish+1):
#     results_for = i * results_for
# print(results_for)



# while a <= finish :
#     result_while = result_while * a
#     a += 1
# print(result_while)

# if result_while == results_for:
#     print("eşit")

# for david in range(29):
#     for emma in range(29):
#         if emma == david + 3 :
#             for frank in range(29):
#                 if frank == david * 3 and frank + david + emma == 28 :
#                     print("David packed ", david ,"cupcakes")

# enter = int(input(">Enter an integer: "))
# remainder =""
# while enter > 0 :
#     a = enter % 2 
#     remainder = str(a) + remainder
#     enter = enter // 2
# print(remainder)

# x = 0 
# for a in range(10):
#     x += 0.1
# if x == 1 :
#     print("equal")
# else:
#     print("not equal")
# print(x)

# find = int(input("Enter a number: "))

# epsilon = 0.01
# num_guesses = 0
# increment = 0.0001

# guess = 1 

# while abs(guess**2 - find) > epsilon :
#     guess = guess + increment
#     num_guesses += 1
#     if num_guesses%1000 == 0: print("Current guess=", guess)
        
# print(guess,num_guesses) 

# enter = int(input("enter a number: "))

# low = 0
# high = 148

# step = 0

# guess = (low + high)/ 2

# while guess != enter:
#     if guess > enter :
#         high = guess
#         guess = (low + high)// 2
#     else:
#         low = guess
#         guess = (low + high)// 2
#     step += 1
# if guess == enter:
#     print("lessssgooo", step)


