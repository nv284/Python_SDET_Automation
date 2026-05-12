from base_page import BasePage

class LoginPage(BasePage):
    def __init__(self):
        super().__init__('Login')
        self._username_field = ''
        self._password_field = ''

    def enter_username(self, u):
        self._username_field = u
        print('Username entered')

    def enter_password(self, p):
        self._password_field = p
        print('Password entered')

    def submit(self):
        # simple validation to simulate business logic
        if self._username_field == 'admin' and self._password_field == 'pass':
            print('LoginPage: login successful')
            return True
        else:
            print('LoginPage: login failed')
            return False
