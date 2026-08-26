class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def check_password(self, input_password):
        if input_password == self.password:
            return True
        else:
            return False
        
u1 = User("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("Juan"))