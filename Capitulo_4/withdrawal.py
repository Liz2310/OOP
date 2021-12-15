class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"account doesn't have ${amount}") # when not handled, the exception displays this message; sending string to BaseException class in order to display said message when raised
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance

# raise InvalidWithdrawal(25, 50)

# try:
#     raise InvalidWithdrawal(25, 50)
# except InvalidWithdrawal as e:
#     print("I'm sorry, but your withdrawal is "
#           "more than your balance by "
#           f"${e.overage()}")

