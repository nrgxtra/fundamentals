salary = 4 * 5000 + 1000 + 3000 + 7000
abroad_income = 10*300*1.95
minus = 6000+2300+2000
monthly = (salary+abroad_income-minus) / 12
debt = 1000
clear_monthly = monthly-debt
daily = clear_monthly/30
print(f'{clear_monthly:.2f}')
print(f'{daily:.2f}')

