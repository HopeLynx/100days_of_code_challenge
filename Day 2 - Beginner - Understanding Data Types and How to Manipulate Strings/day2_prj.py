print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))
tip_perc = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
print(f"Each person should pay: ${round(total * (100+tip_perc) / 100 / num_of_people,2)}")
