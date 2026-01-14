monthly_incomes = [ 5000000, 1500000, 2000000, 2500000 ]
saving_after_tax = []

for income in monthly_incomes:
    if income >= 500000:
        tax = income * 0.30
        status = "High earner : (30% Tax)"
    else:
        tax = income * 0.20
        status = "Rising star (20% Tax)"
        
    in_hand = income - tax
    saving_after_tax.append(in_hand)
    
    total_savings = sum(saving_after_tax)
    print(f"\nTotal savings in 6 months:₹ {total_savings}")
    
    if total_savings > 5000000:
        print("Status: M8 ke payment tayyar hai")
    else:
        print("Status: Aur mehnat ke jarurat hai")
        
    
