class User:
    def __init__(self, username, password):
        self.username=username
        self.password=password

    def check_password(self, input_password):
        if input_password == self.password:
            return True
        else:
            return False

u1 = User("alice", "secure123")
input_password=input("Escribi tu contrasena ")
u1.check_password(input_password)