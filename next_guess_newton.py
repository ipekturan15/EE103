x = float(input("What x to find the square root of?"))
g = float(input("What guess to start with?"))
print("Current estimate squarred:", g*g)
next_g = (g + x / g) / 2
print("Next guess:", next_g)