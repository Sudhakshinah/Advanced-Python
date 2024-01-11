from regex import RegexPattern

data = input(" Enter the password: ")
password = RegexPattern(data)
print(password.password_validation())