class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_balance(self):
        print(f"You have {self.account_balance} in your account.")
    # def transfer(self, username, amount):
    #     self.account_balance -= amount
    #     username.account_balance += amount
    #     print(f"You transfered {amount} to {username.name}")


michael = User("Michael", "michael@yahoo.com")
john = User("John", "johnnyj@gmail.com")
tim = User("Tim", "timmy@sleepytime.com")

michael.make_deposit(87.53)
michael.make_deposit(39.47)
michael.make_deposit(7276.01)
michael.make_withdrawl(100.00)
michael.display_balance()

john.make_deposit(1000)
john.make_deposit(1122)
john.make_withdrawl(1200)
john.display_balance()

tim.make_deposit(5000)
tim.make_withdrawl(1570)
tim.make_withdrawl(3572)
tim.display_balance()

#michael.transfer("tim", 150)