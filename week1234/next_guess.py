x = int(input("What x to find the cube root of?"))

g = int(input("What guess to start with?"))

if g**3 == x:
    print(f'You found it! The cube root of {x} is {g}')

else:
    print(f"Wrong guess. {g} cubed is {g ** 3}, not {x}")
    g = int(input("What guess to start with? "))

# burada sadece 2 kez soruyor ve sonrasında bitiyor while loopu ile döngüde çalıştırabilirsin
