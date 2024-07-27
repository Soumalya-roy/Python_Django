class AuthenticationSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store users and their passwords

    def register(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = password
        print(f"User '{username}' registered successfully.")

    def sign_in(self, username, password):
        if username not in self.users:
            raise ValueError("Username not found.")
        if self.users[username] != password:
            raise ValueError("Incorrect password.")
        print(f"User '{username}' signed in successfully.")
        return True
    
    def view(self):
        for i in self.users:
        print("Username - ",i," Password - ",self.users[i])
    
    def search()

# Example usage
auth_system = AuthenticationSystem()

# Register users
try:
    x=input("Enter name ")
    xp=input("Enter password ")
    y=input("Enter name ")
    yp=input("Enter password ")
    auth_system.register(x,xp)
    auth_system.register(y, yp)
except ValueError as e:
    print(e)

# Attempt to sign in
try:
    x=input("Enter name ")
    xp=input("Enter password ")
    y=input("Enter name ")
    yp=input("Enter password ")
    auth_system.sign_in(x, xp)  # Successful sign-in
    auth_system.sign_in(y, yp)  # Incorrect password
except ValueError as e:
    print(e)

# Try registering an existing user
try:
    x=input("Enter name ")
    xp=input("Enter password ")
    auth_system.register(x,xp)
except ValueError as e:
    print(e)

# Try signing in with a non-existent user
try:
    x=input("Enter name ")
    xp=input("Enter password ")
    auth_system.sign_in(x,xp)
except ValueError as e:
    print(e)
auth_system.view()