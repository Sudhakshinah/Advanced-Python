import re

# parent class


class RegexPattern:
    email_pattern = "(^[A-Za-z_\\.\\-0-9]+)[@]([a-z])+[\\.]([a-z]{2,3})"
    bangladesh_mobile_pattern = "(^(01){1}[3-9]{1}\\d{8}$)"
    usa_phone_pattern = "^\\(?([0-9]{3})\\)?[-.●]?([0-9]{3})[-.●]?([0-9]{4})$"
    password_pattern = "(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{16}$"

    def __init__(self, data):
        self.data = data

    def email_validation(self):
        if re.match(self.email_pattern, self.data):
            return True
        else:
            return False

    def bangladesh_mobile_validation(self):
        if re.match(self.bangladesh_mobile_pattern, self.data):
            return True
        else:
            return False

    def usa_phone_validation(self):
        if re.match(self.usa_phone_pattern, self.data):
            return True
        else:
            return False

    def password_validation(self):
        if re.match(self.password_pattern, self.data):
            return True
        else:
            return False


