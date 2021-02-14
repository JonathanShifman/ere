monthly_active_income = 20_000
monthly_passive_income = 5_000
monthly_expenses = 12_000
annual_expenses = monthly_expenses * 12
monthly_savings = monthly_active_income + monthly_passive_income - monthly_expenses
annual_savings = monthly_savings * 12
monthly_expenses_after_passive = monthly_expenses - monthly_passive_income
annual_expenses_after_passive = 12 * monthly_expenses_after_passive
current_net_worth = 300_000
yearly_yield = 0.06
withdrawal_rate = 0.04

year = 1
yearly_withdrawal = 0
previous_yearly_withdrawal = None
years_to_retirement = None
while True:
    invested_net_worth = current_net_worth + (annual_savings / 2)
    yearly_roi = invested_net_worth * yearly_yield
    previous_yearly_withdrawal = yearly_withdrawal
    yearly_withdrawal = invested_net_worth * withdrawal_rate
    current_net_worth += annual_savings + yearly_roi
    print('Year ' + str(year))
    print('ROI: ' + str(round(yearly_roi)) + ', Withdrawal: ' + str(round(yearly_withdrawal)) + ', Net Worth: ' + str(round(current_net_worth)))
    if yearly_withdrawal >= annual_expenses_after_passive:
        current_year_ratio = (annual_expenses_after_passive - previous_yearly_withdrawal) / (yearly_withdrawal - previous_yearly_withdrawal)
        years_to_retirement = year - 1 + current_year_ratio
        break
    year += 1

print()
print('Years to retirement: ' + str(round(years_to_retirement, 1)))