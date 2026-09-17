class User:
	def __init__(self, username, password):
		self.username = username
		self._password = password

	def check_password(self, input_password):
		return input_password == self._password


u1 = User("alice", "secure123")
print(u1.check_password("secure123"))
print(u1.check_password("wrongpassword"))