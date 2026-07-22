# first print statement 

print("Welcome to tip calculater🙏")

# asigning the values

Bill = float(input("Bill: $"))
Tip = int(input("Tip:"))
People = int(input("No. of people:"))

# calculation part 

amount = Bill * (1 + Tip / 100) / People

# final print statement

print(f"Each person should pay💸${amount:.2f}")