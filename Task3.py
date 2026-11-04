math = int(input("Enter Math Marks 100/"))
english = int(input("Enter English Marks 100/"))
physics = int(input("Enter Physics Marks 100/"))

total = math + english + physics
percentage = total / 300 * 100

print("\n==== RESULT ====")
print(f"Math: {math}")
print(f"English: {english}")
print(f"Physics: {physics}")
print(f"Your Total Marks {total}/300")
print(f"Your Percentage is: {percentage}")
