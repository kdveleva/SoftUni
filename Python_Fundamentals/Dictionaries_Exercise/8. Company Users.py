company_users = {}
while True:
    command = input()
    if command == "End":
        break
    command = command.split(' -> ')
    company_name = command[0]
    employee_id = command[1]
    if company_name not in company_users:
        company_users[company_name] = []
    if employee_id not in company_users[company_name]:
        company_users[company_name].append(employee_id)

sort_company_users = dict(sorted(company_users.items(),
                                 key=lambda x: x))


for key, value in sort_company_users.items():
    print(key)
    for user in value:
        print(f'-- {user}')