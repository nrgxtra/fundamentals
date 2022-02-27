companies = dict()
while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split(' -> ')
    company = tokens[0]
    id_worker = tokens[1]
    if company not in companies:
        companies[company] = []
        companies[company].append(id_worker)
    if id_worker not in companies[company]:
        companies[company].append(id_worker)
companies_s = dict(sorted(companies.items()))
for company, employee in companies_s.items():
    print(company)
    for item in employee:
        print(f'-- {item}')







