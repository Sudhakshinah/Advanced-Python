from regex import RegexPattern

data = input(" Enter the phone-number: ")
usa_phone = RegexPattern(data)
print(usa_phone.usa_phone_validation())