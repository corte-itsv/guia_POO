class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_password(self, input_password):
        if self.password == input_password:
            print(True)
        else:
            print(False)

u1 = User("alice", "secure123")
u1.check_password("secure123")
u1.check_password("tyhtrewrgthgfdsfgthdrew")
