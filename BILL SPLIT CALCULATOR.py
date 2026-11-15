print("Bill Split Calculator")
bill_amount = float(input("What is the bill amount: "))
tip_percentage = float(input("What is the tip percentage: "))
tip_amount = (tip_percentage / 100) * bill_amount
total_amount = bill_amount + tip_amount
print(f"Total (including tip): ${total_amount}")
people_splitting = int(input("How many people are splitting the bill: "))
amount_person = total_amount/people_splitting
print(f"Each person pays: ${amount_person}")