midterm = float(input("Enter your midterm score: "))
final = float(input("Enter your final score: "))

average = 0.4 * midterm + 0.6 * final

print(f"Average: {average:.2f}") 

if average >= 80:
    print("Excellent!")
elif average >= 60:
    print("Passed")
else:
    print("Failed")

