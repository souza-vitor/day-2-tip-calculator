#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people to split the bill? ")

tip = float(bill) * (float(percentage) / 100)
total = float(bill) + float(tip)
total_split = total / int(split)
formated_split = "{:.2f}".format(total_split)

print(f"Each person should pay: {formated_split}")