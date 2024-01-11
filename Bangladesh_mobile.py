from regex import RegexPattern

data = input(" Enter the phone-number: ")
bangla_phone = RegexPattern(data)
print(bangla_phone.bangladesh_mobile_validation())