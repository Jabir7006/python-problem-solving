emails = ["user1@gmail.com", "admin@company.com", "user2@yahoo.com", "manager@company.com"]

company_emails = []

for email in emails:
    if email.endswith('@company.com'):
        company_emails.append(email)


print(company_emails)
