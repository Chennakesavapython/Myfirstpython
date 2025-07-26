car_id = 1
car_variant = "S9 seater diesel"
car_model = "Mahindra Scorpio"
car_price = 1753690.00
car_down_payment = 160000
bank_intrest_rate = 9.0
loan_period_years = 5 

# EMI formula: E = P * r * (1 + r)^n / ((1 + r)^n - 1)

# loan calculator
loan_ampount = car_price - car_down_payment
total_payable_amount = 1753690
monthly_emi = total_payable_amount / (loan_period_years*12)

# conditions
min_down_payment_required = 150000
eligible_for_loan = car_down_payment >= min_down_payment_required


print(f" car model : {car_model }")
print(f" car variant : {car_variant }")
print(f" car on-road price :  {car_price }")
print(f" down payment :  {car_down_payment }")
print(f" loan intrest : {bank_intrest_rate }")
print(f" loan amount : {loan_ampount }")
print(f" loan period : {loan_period_years }")
print(f" mothly emi  : {monthly_emi }")
print(f" eligibility  :  {eligible_for_loan }")