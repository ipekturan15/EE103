# # integer form 7 to 18 multi each number
# outcome = 1
# for i in range(7, 19):
#     outcome *= i
# print(outcome)


# result = ""
# s = "wsshjhwshwnhatsy"

# for i in s:
#     if i in result:
#         continue
#     else:
#         result += i

# print(result)


# Alyssa, Ben, and Cindy Ben sells 2 fewer than Alyssa. 
# Cindy sells twice as many as Alyssa. Ben sells 2 fewer than Alyssa.  10 total tickets were sold by the three people. How many did Alyssa sell? 

# for alyssa in range(11):
#     for ben in range(11):
#         for cindy in range(11):
#             if alyssa + ben + cindy == 10 and ben == alyssa - 2 and cindy == alyssa * 2:
#                 print(f"Alyssa sold {alyssa} tickets, Ben sold {ben} tickets, Cindy sold {cindy} tickets.")

# for alyssa in range(1000):
#     for ben in range(1000):
#         if ben == alyssa - 20:
#             for cindy in range(1000):
#                  if alyssa + ben + cindy == 1000 and ben == alyssa - 20 and cindy == alyssa * 2:
#                       print(f"Alyssa sold {alyssa} tickets, Ben sold {ben} tickets, Cindy sold {cindy} tickets.")

# for alyssa in range(1001):
#     ben = alyssa - 20
#     cindy = alyssa * 2
#     if alyssa + ben + cindy == 1000:
#         print(f"Alyssa sold {alyssa}, Ben sold {ben}, Cindy sold {cindy}.")


# x = 0 
# for i in range(10): 

#     x = x + 0.1 
# print(x)

# binary

# number = 309

# remainders = ""

# while number > 0:
#     remainder = number % 2
#     remainders = str(remainder) + remainders
#     number = number // 2

# print(remainders)

# number = 309
# remainders = ""

# while number > 0:
#     if number % 2 == 1:
#         remainders = "1" + remainders
#     else:
#         remainders = "0" + remainders
#     number = number // 2

# print(remainders)


# number = 0.375
# binary = ""
# count = 0
# # number[0] çalışmaz.
# # number bir float (sayı), string değil. Sayının [0] ile ilk karakterine ulaşamazsın:

# while number > 0 and count < 10:
#     number *= 2
#     if number >= 1 :
#         binary += "1"
#         number -= 1
#     else:
#         binary += "0"
#     count += 1
# print("0." + binary) 


# number = 2.75

# inthali = int(number)
# frac = number - inthali 

# intbinary = ""
# if inthali == 0:
#     intbinary = "0"
# while inthali > 0:
#     intbinary = str(inthali % 2) + intbinary
#     inthali = inthali // 2

# fracbinary = ""
# count = 0


