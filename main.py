print("Welcome to the tip calculator.")
total_bill = input("What is your total bill? $")
per_tip = input("What percentage of tip would you like to give? 10, 12, or 15? ")
split_bill = input("How many people to split the bill? ")
final_tip_pay = round((float(per_tip)/ 100) * float(total_bill) , 2)
total_bill_pay_after_tip = float(final_tip_pay) + float(total_bill)
y = float(total_bill_pay_after_tip) / float(split_bill)
t = f"You are paying a tip of ${final_tip_pay} and you bill after tip will be ${total_bill_pay_after_tip} and after split each will pay ${y}"
print(t)