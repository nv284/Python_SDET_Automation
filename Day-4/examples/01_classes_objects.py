# Classes and objects: simple test entity
class TestUser:
    def __init__(self, username, role='guest'):
        self.username = username
        self.role = role

    def info(self):
        return f'User({self.username}, role={self.role})'

u = TestUser('alice', role='tester')
print(u.info())
