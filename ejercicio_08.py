class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        return self.password == input_password

u1 = User("alice", "secure123")
print(f"{u1.check_password("secure123")}")
print(f"{u1.check_password("holasoylauty")}")