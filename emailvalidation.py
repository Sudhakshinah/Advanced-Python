from regex import RegexPattern

data = input(" Enter the email_id: ")
email = RegexPattern(data)
print(email.email_validation())
