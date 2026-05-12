# Encapsulation and abstraction: exposing simple APIs while hiding internals
class BrowserSession:
    def __init__(self):
        self._cookies = {}  # internal state
        self._logged_in = False

    def login(self, user, pw):
        # simplified login simulation
        if user == 'admin' and pw == 'pass':
            self._logged_in = True
            self._cookies['session'] = 'XYZ123'
            print('Login successful')
        else:
            print('Login failed')

    def is_authenticated(self):
        return self._logged_in

s = BrowserSession()
s.login('admin', 'pass')
print('Authenticated?', s.is_authenticated())
