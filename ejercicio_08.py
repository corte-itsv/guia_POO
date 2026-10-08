class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def chek_password(self, input_password):
        if input_password == self.password:
            return True
        else:
            return False
        
u1 = User("alice", "secure123")
primer_check = u1.chek_password("secure123")
print(primer_check)

segundo_check = u1.chek_password("seguridad123")
print(segundo_check)