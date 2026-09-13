class user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, contraseña):
        return self.password == contraseña

u1 = user("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("wrongpassword"))