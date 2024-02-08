#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = (float(input("What was the total bill? ")))
tip = float(input("How much would you like to tip? (10%, 12%, or 15%) "))

people = int(input("Split by how many people? "))

tip_amount = int(bill * (tip * .01))
total_bill = bill + tip_amount

per_person = total_bill / people

print(f"Each person should pay: ${round(per_person, 2)}")

